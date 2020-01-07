# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'frm_dbSettings.ui'
#
# Created: Sat Aug 30 21:32:57 2014
#      by: PyQt4 UI code generator 4.11.1
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
        MainWindow.resize(360, 248)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        spacerItem = QtGui.QSpacerItem(0, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.lineEdit_host = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_host.setObjectName(_fromUtf8("lineEdit_host"))
        self.horizontalLayout.addWidget(self.lineEdit_host)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_2.addWidget(self.label_2)
        spacerItem1 = QtGui.QSpacerItem(35, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.lineEdit_port = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_port.setObjectName(_fromUtf8("lineEdit_port"))
        self.horizontalLayout_2.addWidget(self.lineEdit_port)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.label_4 = QtGui.QLabel(self.centralwidget)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.horizontalLayout_3.addWidget(self.label_4)
        spacerItem2 = QtGui.QSpacerItem(5, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.lineEdit_db = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_db.setObjectName(_fromUtf8("lineEdit_db"))
        self.horizontalLayout_3.addWidget(self.lineEdit_db)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.label_5 = QtGui.QLabel(self.centralwidget)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.horizontalLayout_4.addWidget(self.label_5)
        spacerItem3 = QtGui.QSpacerItem(15, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem3)
        self.lineEdit_schema = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_schema.setObjectName(_fromUtf8("lineEdit_schema"))
        self.horizontalLayout_4.addWidget(self.lineEdit_schema)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.label_6 = QtGui.QLabel(self.centralwidget)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.horizontalLayout_5.addWidget(self.label_6)
        spacerItem4 = QtGui.QSpacerItem(0, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem4)
        self.lineEdit_username = QtGui.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.lineEdit_username.setFont(font)
        self.lineEdit_username.setObjectName(_fromUtf8("lineEdit_username"))
        self.horizontalLayout_5.addWidget(self.lineEdit_username)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.label_7 = QtGui.QLabel(self.centralwidget)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.horizontalLayout_6.addWidget(self.label_7)
        spacerItem5 = QtGui.QSpacerItem(3, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem5)
        self.lineEdit_password = QtGui.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.lineEdit_password.setFont(font)
        self.lineEdit_password.setInputMethodHints(QtCore.Qt.ImhHiddenText|QtCore.Qt.ImhNoAutoUppercase|QtCore.Qt.ImhNoPredictiveText)
        self.lineEdit_password.setEchoMode(QtGui.QLineEdit.Password)
        self.lineEdit_password.setObjectName(_fromUtf8("lineEdit_password"))
        self.horizontalLayout_6.addWidget(self.lineEdit_password)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.buttonBox = QtGui.QDialogButtonBox(self.centralwidget)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Save)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout.addWidget(self.buttonBox)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 360, 19))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Database Connection Settings", None))
        self.label.setText(_translate("MainWindow", "Hostname:", None))
        self.label_2.setText(_translate("MainWindow", "Port:", None))
        self.label_4.setText(_translate("MainWindow", "Database:", None))
        self.label_5.setText(_translate("MainWindow", "Schema:", None))
        self.label_6.setText(_translate("MainWindow", "Username:", None))
        self.label_7.setText(_translate("MainWindow", "Password:", None))

