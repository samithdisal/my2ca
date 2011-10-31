# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'select_tables_page.ui'
#
# Created: Tue Nov  1 00:36:31 2011
#      by: pyside-uic 0.2.12 running on PySide 1.0.5
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(653, 399)
        self.horizontalLayout = QtGui.QHBoxLayout(Form)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.availableTableList = QtGui.QListWidget(Form)
        self.availableTableList.setObjectName("availableTableList")
        self.horizontalLayout.addWidget(self.availableTableList)
        self.widget = QtGui.QWidget(Form)
        self.widget.setObjectName("widget")
        self.verticalLayout = QtGui.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.addButton = QtGui.QPushButton(self.widget)
        self.addButton.setObjectName("addButton")
        self.verticalLayout.addWidget(self.addButton)
        self.addAllButton = QtGui.QPushButton(self.widget)
        self.addAllButton.setObjectName("addAllButton")
        self.verticalLayout.addWidget(self.addAllButton)
        self.removeButton = QtGui.QPushButton(self.widget)
        self.removeButton.setObjectName("removeButton")
        self.verticalLayout.addWidget(self.removeButton)
        self.removeAllButton = QtGui.QPushButton(self.widget)
        self.removeAllButton.setObjectName("removeAllButton")
        self.verticalLayout.addWidget(self.removeAllButton)
        self.horizontalLayout.addWidget(self.widget)
        self.selectedTableList = QtGui.QListWidget(Form)
        self.selectedTableList.setObjectName("selectedTableList")
        self.horizontalLayout.addWidget(self.selectedTableList)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.addButton.setText(QtGui.QApplication.translate("Form", "Add", None, QtGui.QApplication.UnicodeUTF8))
        self.addAllButton.setText(QtGui.QApplication.translate("Form", "Add All", None, QtGui.QApplication.UnicodeUTF8))
        self.removeButton.setText(QtGui.QApplication.translate("Form", "Remove", None, QtGui.QApplication.UnicodeUTF8))
        self.removeAllButton.setText(QtGui.QApplication.translate("Form", "Remove All", None, QtGui.QApplication.UnicodeUTF8))

