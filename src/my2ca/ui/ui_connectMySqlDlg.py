# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'connectMySqlDlg.ui'
#
# Created: Mon Oct 31 23:50:14 2011
#      by: pyside-uic 0.2.12 running on PySide 1.0.5
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_connectMySqlDlg(object):
    def setupUi(self, connectMySqlDlg):
        connectMySqlDlg.setObjectName("connectMySqlDlg")
        connectMySqlDlg.setWindowModality(QtCore.Qt.ApplicationModal)
        connectMySqlDlg.resize(378, 173)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(connectMySqlDlg.sizePolicy().hasHeightForWidth())
        connectMySqlDlg.setSizePolicy(sizePolicy)
        connectMySqlDlg.setModal(True)
        self.verticalLayout = QtGui.QVBoxLayout(connectMySqlDlg)
        self.verticalLayout.setSizeConstraint(QtGui.QLayout.SetDefaultConstraint)
        self.verticalLayout.setObjectName("verticalLayout")
        self.formLayout = QtGui.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label = QtGui.QLabel(connectMySqlDlg)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label)
        self.hostE = QtGui.QLineEdit(connectMySqlDlg)
        self.hostE.setObjectName("hostE")
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.hostE)
        self.label_2 = QtGui.QLabel(connectMySqlDlg)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_2)
        self.userE = QtGui.QLineEdit(connectMySqlDlg)
        self.userE.setObjectName("userE")
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.userE)
        self.label_3 = QtGui.QLabel(connectMySqlDlg)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_3)
        self.passE = QtGui.QLineEdit(connectMySqlDlg)
        self.passE.setEchoMode(QtGui.QLineEdit.Password)
        self.passE.setObjectName("passE")
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.passE)
        self.label_5 = QtGui.QLabel(connectMySqlDlg)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(3, QtGui.QFormLayout.LabelRole, self.label_5)
        self.dbE = QtGui.QLineEdit(connectMySqlDlg)
        self.dbE.setObjectName("dbE")
        self.formLayout.setWidget(3, QtGui.QFormLayout.FieldRole, self.dbE)
        self.label_4 = QtGui.QLabel(connectMySqlDlg)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(4, QtGui.QFormLayout.LabelRole, self.label_4)
        self.portE = QtGui.QLineEdit(connectMySqlDlg)
        self.portE.setObjectName("portE")
        self.formLayout.setWidget(4, QtGui.QFormLayout.FieldRole, self.portE)
        self.verticalLayout.addLayout(self.formLayout)
        self.buttonBox = QtGui.QDialogButtonBox(connectMySqlDlg)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(connectMySqlDlg)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), connectMySqlDlg.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), connectMySqlDlg.reject)
        QtCore.QMetaObject.connectSlotsByName(connectMySqlDlg)

    def retranslateUi(self, connectMySqlDlg):
        connectMySqlDlg.setWindowTitle(QtGui.QApplication.translate("connectMySqlDlg", "Connect MySQL Database", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("connectMySqlDlg", "Host", None, QtGui.QApplication.UnicodeUTF8))
        self.hostE.setText(QtGui.QApplication.translate("connectMySqlDlg", "localhost", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("connectMySqlDlg", "Username", None, QtGui.QApplication.UnicodeUTF8))
        self.userE.setText(QtGui.QApplication.translate("connectMySqlDlg", "root", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("connectMySqlDlg", "Password", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("connectMySqlDlg", "Database", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("connectMySqlDlg", "Port", None, QtGui.QApplication.UnicodeUTF8))
        self.portE.setText(QtGui.QApplication.translate("connectMySqlDlg", "3306", None, QtGui.QApplication.UnicodeUTF8))

