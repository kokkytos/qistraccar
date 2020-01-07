# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\TIMOLOGISI\.qgis2\python\plugins\traccar\search.ui'
#
# Created: Mon Mar 09 12:34:44 2015
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(800, 600)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 0, 1, 1, 1)
        self.timeEdit_2 = QtGui.QTimeEdit(self.centralwidget)
        self.timeEdit_2.setCalendarPopup(False)
        self.timeEdit_2.setObjectName(_fromUtf8("timeEdit_2"))
        self.gridLayout.addWidget(self.timeEdit_2, 2, 2, 1, 1)
        self.dateEdit_2 = QtGui.QDateEdit(self.centralwidget)
        self.dateEdit_2.setCalendarPopup(True)
        self.dateEdit_2.setObjectName(_fromUtf8("dateEdit_2"))
        self.gridLayout.addWidget(self.dateEdit_2, 2, 1, 1, 1)
        self.dateEdit = QtGui.QDateEdit(self.centralwidget)
        self.dateEdit.setCalendarPopup(True)
        self.dateEdit.setObjectName(_fromUtf8("dateEdit"))
        self.gridLayout.addWidget(self.dateEdit, 1, 1, 1, 1)
        self.comboBox = QtGui.QComboBox(self.centralwidget)
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.gridLayout.addWidget(self.comboBox, 0, 2, 1, 1)
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 3, 4, 1, 1)
        self.timeEdit = QtGui.QTimeEdit(self.centralwidget)
        self.timeEdit.setCalendarPopup(False)
        self.timeEdit.setObjectName(_fromUtf8("timeEdit"))
        self.gridLayout.addWidget(self.timeEdit, 1, 2, 1, 1)
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 1, 3, 1, 1)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 2, 3, 1, 1)
        self.btnSearch = QtGui.QPushButton(self.centralwidget)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/plugins/traccar/Magnifier-icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnSearch.setIcon(icon)
        self.btnSearch.setIconSize(QtCore.QSize(16, 16))
        self.btnSearch.setObjectName(_fromUtf8("btnSearch"))
        self.gridLayout.addWidget(self.btnSearch, 3, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.lblLength = QtGui.QLabel(self.centralwidget)
        self.lblLength.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lblLength.setObjectName(_fromUtf8("lblLength"))
        self.horizontalLayout.addWidget(self.lblLength)
        self.lineEdit = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.horizontalLayout.addWidget(self.lineEdit)
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.tableView = QtGui.QTableView(self.centralwidget)
        self.tableView.setObjectName(_fromUtf8("tableView"))
        self.verticalLayout.addWidget(self.tableView)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtGui.QToolBar(MainWindow)
        self.toolBar.setObjectName(_fromUtf8("toolBar"))
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.action_AddtoMap = QtGui.QAction(MainWindow)
        self.action_AddtoMap.setEnabled(True)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/plugins/traccar/map_add.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_AddtoMap.setIcon(icon1)
        self.action_AddtoMap.setObjectName(_fromUtf8("action_AddtoMap"))
        self.action_Export2kml = QtGui.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/plugins/traccar/Keyhole_Markup_Language.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_Export2kml.setIcon(icon2)
        self.action_Export2kml.setObjectName(_fromUtf8("action_Export2kml"))
        self.action_export2ods = QtGui.QAction(MainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8(":/plugins/traccar/1425482625_OpenOffice_Calc.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_export2ods.setIcon(icon3)
        self.action_export2ods.setObjectName(_fromUtf8("action_export2ods"))
        self.toolBar.addAction(self.action_AddtoMap)
        self.toolBar.addAction(self.action_Export2kml)
        self.toolBar.addAction(self.action_export2ods)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.label_3.setText(_translate("MainWindow", "Συσκευή:", None))
        self.label_2.setText(_translate("MainWindow", "Λήξη:", None))
        self.label.setText(_translate("MainWindow", "Έναρξη:", None))
        self.btnSearch.setText(_translate("MainWindow", "Αναζήτηση", None))
        self.lblLength.setText(_translate("MainWindow", "Μήκος διαδρομής", None))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar", None))
        self.action_AddtoMap.setText(_translate("MainWindow", "Προσθήκη στον χάρτη", None))
        self.action_AddtoMap.setToolTip(_translate("MainWindow", "Προσθήκη στον χάρτη", None))
        self.action_Export2kml.setText(_translate("MainWindow", "Εξαγωγή σε kml", None))
        self.action_Export2kml.setToolTip(_translate("MainWindow", "Εξαγωγή σε kml", None))
        self.action_export2ods.setText(_translate("MainWindow", "Εξαγωγή σε ods", None))
        self.action_export2ods.setToolTip(_translate("MainWindow", "Εξαγωγή σε ods", None))

import resources_rc
