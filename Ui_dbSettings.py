# -*- coding: utf-8 -*-

from PyQt4 import QtGui, QtSql
from PyQt4.QtGui import *

from frm_dbSettings import Ui_MainWindow
import mysettings
from qgis.core import *
from mydatabasemodel import MyDatabaseModel


# create the dialog for paradosiakoioikismoi
class dbSettings_Dialog(QtGui.QMainWindow):
    """Class to handle db connection settings"""

    def __init__(self): 
      
        QtGui.QMainWindow.__init__(self) 

        # Set up the user interface from Designer.
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.lb = QLabel()
        self.lb.setFrameStyle(QtGui.QFrame.Panel | QtGui.QFrame.Sunken)

        # some attributes
        self.dbdriver = None
        self.host = None
        self.port = None
        self.schema = None
        self.username = None
        self.password = None
        self.dbname = None

        reload(mysettings)

        self.db = MyDatabaseModel(mysettings.QSQLDATABASENAME).db  # QSQLDATABASENAME from mysettings

        print "My DB is opened:", self.db.isOpen()
        
        if not self.db.isOpen():

            ok = self.db.open()
            if not ok:
                self.lb.setText(u"<font color='red'>Αποτυχία σύνδεσης...</font>")

        if self.db.isOpen():
            self.lb.setText(u"<font color='green'>Επιτυχής σύνδεση!</font>")

        #  add widget label to statusBar
        self.statusBar().addWidget(self.lb, 0)

        self.ui.lineEdit_host.setText(mysettings.HOST)
        self.ui.lineEdit_port.setText(str(mysettings.PORT))
        self.ui.lineEdit_schema.setText(mysettings.SCHEMA)
        self.ui.lineEdit_username.setText(mysettings.USERNAME)
        self.ui.lineEdit_password.setText(mysettings.PASSWORD)
        self.ui.lineEdit_db.setText(mysettings.DBNAME)

        #  signals and slots
        self.ui.buttonBox.accepted.connect(self.accept)
        self.ui.buttonBox.rejected.connect(self.close)
        
    def accept(self):

        params = self.set_settings()

        #  write settings to file settings.cfg
        mysettings.write(**params)
        
        if self.db.isOpen:
            self.db.close()
            del self.db
            QtSql.QSqlDatabase.removeDatabase(mysettings.QSQLDATABASENAME)
             
            self.db = QtSql.QSqlDatabase.addDatabase(self.dbdriver, mysettings.QSQLDATABASENAME )
            self.db.setHostName(self.host)
            self.db.setPort(int(self.port))
            self.db.setDatabaseName(self.dbname)

            self.db = QtSql.QSqlDatabase.database(mysettings.QSQLDATABASENAME) #ανοίγει ταυτόχρονα και η σύνδεση:
            self.db.open(self.username, self.password)

        if not self.db.isOpen():

            ok = self.db.open()
            if not ok:
                print "Failed to open database!"
                error = self.db.lastError()
                print error.text()
                self.lb.setText(u"<font color='red'>Αποτυχία σύνδεσης...</font>")
                QMessageBox.warning(None,u"Ενημέρωση!",error.text())

        if self.db.isOpen():
            self.lb.setText(u"<font color='green'>Επιτυχής σύνδεση!</font>")
            QMessageBox.information(None,u"Ενημέρωση!",u"Επιτυχία σύνδεσης στην βάση δεδομένων.")

    def set_settings(self):
        """Setup database connection class attributes"""
        self.dbdriver = mysettings.DBDRIVER
        self.host = self.ui.lineEdit_host.text()
        self.port = int(self.ui.lineEdit_port.text())
        self.schema = self.ui.lineEdit_schema.text()
        self.username = self.ui.lineEdit_username.text()
        self.password = self.ui.lineEdit_password.text()
        self.dbname = self.ui.lineEdit_db.text()

        #  init a dict with params
        args = {
                "host": self.host,
                "dbname": self.dbname,
                "port": self.port,
                "schema": self.schema,
                "username": self.username,
                "password": self.password
        }
        return args
