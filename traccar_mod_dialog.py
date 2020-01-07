# -*- coding: utf-8 -*-
"""
/***************************************************************************
 traccarDialog
                                 A QGIS plugin
 Qgis plugin for Traccar, the open source system for various GPS tracking devices
                             -------------------
        begin                : 2015-03-09
        git sha              : $Format:%H$
        copyright            : (C) 2015 by Leonidas Liakos
        email                : leonidas_liakos@yahoo.gr
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4 import QtCore, QtGui, QtSql

from search import Ui_MainWindow
import myfunctions
from mysettings import *
from qgis.core import *
import qgis.utils
import myods
import kmlgenerator
import time
from mydatabasemodel import MyDatabaseModel
from genericthread import GenericThread

class traccarDialog(QtGui.QMainWindow):
    def __init__(self):
        """Constructor."""
        QtGui.QMainWindow.__init__(self)
        # Set up the user interface from Designer.
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # instance attributes
        self.iface = qgis.utils.iface
        self.devicename = None
        self.deviceid = None
        self.route_length = None
        self.kmlfilename = None
        self.odsfilename = None
        self.genericThread2 = None
        self.genericThread3 = None
        self.mymodel = None
        self.StartDateTime = None
        self.EndDateTime = None
        self.fun_sql = None
        self.fun_sql_line = None

        # database and model
        self.traccardb = MyDatabaseModel(QSQLDATABASENAME)  # QSQLDATABASENAME from mysettings
        self.modelDevice = self.traccardb.set_mymodel(SQL_DEVICES)

        # configure devices combobox
        self.conf_combobox(combobox=self.ui.comboBox)

        # set qdateedits to current date
        yesterday = QDate.currentDate().addDays(-1)
        self.ui.dateEdit.setDate(yesterday)
        self.ui.dateEdit_2.setDate(QDate.currentDate())

        # set qtimeedits to current time
        self.ui.timeEdit.setTime(QTime.currentTime())
        self.ui.timeEdit_2.setTime(QTime.currentTime())

        # progress bar, label inside status bar
        self.progressbar = QtGui.QProgressBar()
        self.progressbar.setMinimum(1)
        self.label = QtGui.QLabel(u"<font color='blue'><b>Παρακαλώ περιμένετε...<b></font>")
        self.ui.statusbar.addWidget(self.progressbar)
        self.ui.statusbar.addWidget(self.label)
        self.ui.statusbar.hide()

        # signal and slots
        self.ui.btnSearch.clicked.connect(self.search_positions)
        self.ui.action_AddtoMap.triggered.connect(self.showdataonmap)
        self.ui.action_export2ods.triggered.connect(self.export2ods)
        self.ui.action_Export2kml.triggered.connect(self.export2kml)

    def conf_combobox(self, combobox=None, modelcolumn=1, currentindex=0):
        """set up some settings for combobox"""
        combobox.setModel(self.modelDevice)
        combobox.setModelColumn(modelcolumn)
        combobox.setCurrentIndex(currentindex)

    def search_positions(self):
        # deviceid
        record = self.modelDevice.record(self.ui.comboBox.currentIndex())
        self.deviceid = record.value(0)

        # Dates
        startdate = self.ui.dateEdit.date().toString("yyyy-MM-dd").encode("ascii")  # start date
        enddate = self.ui.dateEdit_2.date().toString("yyyy-MM-dd").encode("ascii")  # end date

        starttime = self.ui.timeEdit.time().toString("HH:mm:ss").encode("ascii")  # start time
        endtime = self.ui.timeEdit_2.time().toString("HH:mm:ss").encode("ascii")  # end time

        self.StartDateTime = "%s %s" % (startdate, starttime)  # Start date-time to pass to postgresql function
        self.EndDateTime = "%s %s" % (enddate, endtime)  # End date-time to pass to postgresql function

        # Generate point model
        self.fun_sql = SQL_FUN_POS_DEV_BETWN_DATE % (
            int(self.deviceid), self.StartDateTime, self.EndDateTime)
        print self.fun_sql

        positionsmodel = QtSql.QSqlQueryModel()
        positionsmodel.setQuery(self.fun_sql, self.traccardb.db)
        sortcolumn = positionsmodel.record().indexOf("time")
        # filterColumn=positionsmodel.record().indexOf("") USELESS

        QApplication.setOverrideCursor(QCursor(Qt.WaitCursor))

        self.ui.tableView.setModel(positionsmodel)
        self.ui.tableView.setVisible(False)
        self.ui.tableView.resizeColumnsToContents()
        self.ui.tableView.setVisible(True)
        self.ui.tableView.setSortingEnabled(True)
        self.ui.tableView.setAlternatingRowColors(True)
        self.ui.tableView.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.ui.tableView.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.ui.tableView.verticalHeader().setVisible(False)

        # κάνω το sort στο tableview γιατί στο QSortFilterProxyModel
        # δεν δουλεύει όταν το datasource είναι QSqlQueryModel
        self.ui.tableView.sortByColumn(sortcolumn, QtCore.Qt.AscendingOrder)

        for field in ["the_geom", "other", "device_id"]:
            columnindex = positionsmodel.record().indexOf(field)
            self.ui.tableView.setColumnHidden(columnindex, True)

        # Generate Line model
        self.fun_sql_line = SQL_FUN_POLYLINE_DEV_BETWN_DATE % (
            int(self.deviceid), self.StartDateTime, self.EndDateTime)
        print self.fun_sql_line

        linemodel = QtSql.QSqlQueryModel(self)
        linemodel.setQuery(self.fun_sql_line, self.traccardb.db)

        mapper = QDataWidgetMapper()
        mapper.setModel(linemodel)

        mapper.addMapping(self.ui.lineEdit, 3)
        mapper.toFirst()

        QApplication.restoreOverrideCursor()

    def export2ods(self):
        """Export data to ods"""

        self.mymodel = self.ui.tableView.model()

        # check for valid model
        if not self.check_valid_model(self.mymodel):
            return

        fn = QtGui.QFileDialog.getSaveFileName(None, 'Save File', os.getenv('HOME'), u"Αρχεία ods (*.ods)")
        if not fn:
            return

        self.odsfilename = myfunctions.fix_file_extension(fn, '.ods')

        # set state of widgets
        self.set_widgets_state()

        # initialize threads and disconnect and reconnect signals to fuctions
        self.genericThread3 = GenericThread(self.generate_ods_stigmata, self.mymodel)
        self.disconnect(self, QtCore.SIGNAL("sendpositions"), self.write_kml)
        self.disconnect(self, QtCore.SIGNAL("finishsavingods"), self.done_info)

        self.connect(self, QtCore.SIGNAL("updateprogressbar"), lambda i: self.progressbar.setValue(i))
        self.connect(self, QtCore.SIGNAL("finishsavingods"), self.done_info)
        self.genericThread3.start()

    def check_valid_model(self, model):
        """Checks if a model is not set or has no rows"""
        if not model:
            QMessageBox.information(None, u"Ενημέρωση!", u"Παρακαλώ κάντε αναζήτηση δεδομένων")
            return
        if model.rowCount() == 0:
            QMessageBox.information(None, u"Ενημέρωση!", u"Δεν βρέθηκαν δεδομένα προς εξαγωγή")
            return
        return True

    def done_info(self, filetype):
        self.progressbar.setValue(self.progressbar.maximum())
        time.sleep(0.5)
        self.ui.statusbar.hide()
        QMessageBox.information(None, u"Ενημέρωση!", u"Η εξαγωγή σε {} ολοκληρώθηκε!".format(filetype))

    def generate_ods_stigmata(self, mymodel):
        stigmata = []
        # device_name,startdate, enddate, route_length,points to initialize new myroute of myobs module
        self.devicename = self.ui.comboBox.currentText()
        self.route_length = self.ui.lineEdit.text()

        for i in range(mymodel.rowCount()):
            myid = mymodel.data(mymodel.index(i, 0))
            address = mymodel.data(mymodel.index(i, 1))
            altitude = mymodel.data(mymodel.index(i, 2))
            course = int(mymodel.data(mymodel.index(i, 3)))
            latitude = mymodel.data(mymodel.index(i, 4))
            longtitude = mymodel.data(mymodel.index(i, 5))
            power = mymodel.data(mymodel.index(i, 7))
            speed = mymodel.data(mymodel.index(i, 8))
            mytime = mymodel.data(mymodel.index(i, 9)).toString("yyyy-MM-dd HH:mm:ss")
            valid = mymodel.data(mymodel.index(i, 10))

            point = myods.stigma(myid, valid, mytime, latitude, longtitude, altitude, speed, course, power, address)
            stigmata.append(point)
            self.emit(QtCore.SIGNAL('updateprogressbar'), i)

        odsobj = myods.myroute(self.devicename, self.StartDateTime, self.EndDateTime,
                               self.route_length, stigmata)
        odsobj.save(self.odsfilename)
        self.emit(QtCore.SIGNAL('finishsavingods'), 'ods')

    def generate_kml_stigmata(self, mymodel):
        """Generates points for kml using kmlgenerator.
        Emits a signal named sendpositions and an argument (stigmata) for use in threads"""
        stigmata = []
        for i in range(mymodel.rowCount()):
            myid = mymodel.data(mymodel.index(i, 0))
            altitude = mymodel.data(mymodel.index(i, 2))
            latitude = mymodel.data(mymodel.index(i, 4))
            longtitude = mymodel.data(mymodel.index(i, 5))
            mytime = mymodel.data(mymodel.index(i, 9)).toString("yyyy-MM-dd HH:mm:ss")

            kmlposition = kmlgenerator.Position(u"Σημείο %s" % myid, latitude, longtitude, altitude, mytime)
            stigmata.append(kmlposition)
            self.emit(QtCore.SIGNAL('updateprogressbar'), i)

        self.emit(QtCore.SIGNAL('sendpositions'), stigmata)

    def export2kml(self):
        """export data to kml"""

        print 'export data to kml'
        self.mymodel = self.ui.tableView.model()

        # check for valid model
        if not self.check_valid_model(self.mymodel):
            return

        fn = QtGui.QFileDialog.getSaveFileName(None, 'Save File', os.getenv('HOME'), u"Αρχεία kml (*.kml)")

        if not fn:
            return

        self.kmlfilename = myfunctions.fix_file_extension(fn, '.kml')

        # set state of widgets
        self.set_widgets_state()

        # generic thread using signal
        self.genericThread2 = GenericThread(self.generate_kml_stigmata, self.mymodel)
        self.disconnect(self, QtCore.SIGNAL("sendpositions"), self.write_kml)

        # connect signal "sendpositions" with method write_kml
        self.connect(self, QtCore.SIGNAL("sendpositions"), self.write_kml)

        self.connect(self, QtCore.SIGNAL("updateprogressbar"), lambda i: self.progressbar.setValue(i))
        self.genericThread2.start()

    def write_kml(self, stigmata):
        """Call kmlgenerator and write to disk"""
        try:
            mykml = kmlgenerator.kmlobj(stigmata)
            mykml.writekml2disk(self.kmlfilename)
            self.done_info('kml')
        except:
            QMessageBox.information(None, u"Ενημέρωση!", u"Δεν ήταν δυνατή η εξαγωγή σε kml!")

    def set_widgets_state(self):
        """set state of widgets"""
        self.progressbar.setMaximum(self.mymodel.rowCount()+150)
        self.progressbar.show()
        self.ui.statusbar.show()

    def addlayers2toc(self):
        """Loads postgis layer to TOC"""
        # add to map
        if not self.postgislayer:
            self.ui.statusbar.hide()
            QMessageBox.critical(None, u'Σφάλμα', u'Το layer δεν είναι έγκυρο!')
            return

        if not self.postgislayer_line:
            self.ui.statusbar.hide()
            QMessageBox.critical(None, u'Σφάλμα', u'Το layer δεν είναι έγκυρο!')
            return

        self.devicegroup = self.iface.legendInterface().addGroup(
                u"%s-%s-%s" % (self.ui.comboBox.currentText(), self.StartDateTime, self.EndDateTime))

        self.pointsLayer = QgsMapLayerRegistry.instance().addMapLayer(self.postgislayer)
        self.linelayer = QgsMapLayerRegistry.instance().addMapLayer(self.postgislayer_line)

        self.iface.legendInterface().moveLayer(self.pointsLayer, self.devicegroup)
        self.iface.legendInterface().moveLayer(self.linelayer, self.devicegroup)

        self.done_info("postgis layer") # Call the info function

    def showdataonmap(self):

        #first show widgets
        self.progressbar.hide()
        self.ui.statusbar.show()

        # thread using signal to load postgis layers
        self.genericThread = GenericThread(self.loadpostgislayers)
        self.disconnect(self, QtCore.SIGNAL("displayonmap"), self.addlayers2toc)

        # connect signal "sendpositions" with method write_kml
        self.connect(self, QtCore.SIGNAL("displayonmap"), self.addlayers2toc)

        self.genericThread.start()

    def loadpostgislayers(self):
        """loads postgis layers objects for points and line and emits a signal to call another function"""
        try:
            #set wait cursor
            QApplication.setOverrideCursor(QCursor(Qt.WaitCursor))

            # create a new postgis layer
            self.postgislayer = myfunctions.addPostGISLayer(HOST, PORT, DBNAME, USERNAME, PASSWORD, '',
                                                       u"(%s)" % self.fun_sql, u"Στίγματα:%s-%s-%s" % (
                                                           self.ui.comboBox.currentText(), self.StartDateTime,
                                                           self.EndDateTime), 'the_geom', 'id')
            self.postgislayer_line = myfunctions.addPostGISLayer(HOST, PORT, DBNAME, USERNAME, PASSWORD, '',
                                                            u"(%s)" % self.fun_sql_line, u"Διαδρομή:%s-%s-%s" % (
                                                                self.ui.comboBox.currentText(), self.StartDateTime,
                                                                self.EndDateTime), 'the_geom', 'device_id')
        except AttributeError:
            print "No data"
        finally:
            # set wait cursor
             QApplication.restoreOverrideCursor()
             self.emit(QtCore.SIGNAL('displayonmap'))
