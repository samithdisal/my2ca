# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'select_tables_page.ui'
#
# Created: Tue Jul 17 01:01:13 2012
#      by: pyside-uic 0.2.11 running on PySide 1.0.6
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_selectTablesPage(object):
    def setupUi(self, selectTablesPage):
        selectTablesPage.setObjectName("selectTablesPage")
        selectTablesPage.resize(653, 399)
        self.horizontalLayout = QtGui.QHBoxLayout(selectTablesPage)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.availableTableList = QtGui.QListWidget(selectTablesPage)
        self.availableTableList.setObjectName("availableTableList")
        self.horizontalLayout.addWidget(self.availableTableList)
        self.widget = QtGui.QWidget(selectTablesPage)
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
        self.selectedTableList = QtGui.QListWidget(selectTablesPage)
        self.selectedTableList.setObjectName("selectedTableList")
        self.horizontalLayout.addWidget(self.selectedTableList)

        self.retranslateUi(selectTablesPage)
        QtCore.QMetaObject.connectSlotsByName(selectTablesPage)

    def retranslateUi(self, selectTablesPage):
        selectTablesPage.setWindowTitle(QtGui.QApplication.translate("selectTablesPage", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.addButton.setText(QtGui.QApplication.translate("selectTablesPage", "Add", None, QtGui.QApplication.UnicodeUTF8))
        self.addAllButton.setText(QtGui.QApplication.translate("selectTablesPage", "Add All", None, QtGui.QApplication.UnicodeUTF8))
        self.removeButton.setText(QtGui.QApplication.translate("selectTablesPage", "Remove", None, QtGui.QApplication.UnicodeUTF8))
        self.removeAllButton.setText(QtGui.QApplication.translate("selectTablesPage", "Remove All", None, QtGui.QApplication.UnicodeUTF8))

