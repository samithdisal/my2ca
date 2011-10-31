# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created: Tue Nov  1 00:50:36 2011
#      by: pyside-uic 0.2.12 running on PySide 1.0.5
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 599)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.widget = QtGui.QWidget(self.centralwidget)
        self.widget.setObjectName("widget")
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.widget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.connectButton = QtGui.QPushButton(self.widget)
        self.connectButton.setObjectName("connectButton")
        self.horizontalLayout_2.addWidget(self.connectButton)
        self.codegenButton = QtGui.QPushButton(self.widget)
        self.codegenButton.setObjectName("codegenButton")
        self.horizontalLayout_2.addWidget(self.codegenButton)
        self.gridLayout.addWidget(self.widget, 0, 0, 1, 1)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.erdArea = QtGui.QScrollArea(self.centralwidget)
        self.erdArea.setWidgetResizable(True)
        self.erdArea.setObjectName("erdArea")
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 784, 509))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.tablesList = QtGui.QListView(self.scrollAreaWidgetContents)
        self.tablesList.setGeometry(QtCore.QRect(0, -10, 393, 515))
        self.tablesList.setObjectName("tablesList")
        self.erdArea.setWidget(self.scrollAreaWidgetContents)
        self.horizontalLayout.addWidget(self.erdArea)
        self.gridLayout.addLayout(self.horizontalLayout, 1, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 20))
        self.menubar.setObjectName("menubar")
        self.menu_File = QtGui.QMenu(self.menubar)
        self.menu_File.setObjectName("menu_File")
        self.menu_Help = QtGui.QMenu(self.menubar)
        self.menu_Help.setObjectName("menu_Help")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.action_Connect = QtGui.QAction(MainWindow)
        self.action_Connect.setObjectName("action_Connect")
        self.action_Save_Project = QtGui.QAction(MainWindow)
        self.action_Save_Project.setObjectName("action_Save_Project")
        self.action_New_Project = QtGui.QAction(MainWindow)
        self.action_New_Project.setObjectName("action_New_Project")
        self.action_Open_Project = QtGui.QAction(MainWindow)
        self.action_Open_Project.setObjectName("action_Open_Project")
        self.actionE_xit = QtGui.QAction(MainWindow)
        self.actionE_xit.setObjectName("actionE_xit")
        self.action_Context_Help = QtGui.QAction(MainWindow)
        self.action_Context_Help.setObjectName("action_Context_Help")
        self.action_About = QtGui.QAction(MainWindow)
        self.action_About.setObjectName("action_About")
        self.menu_File.addAction(self.action_Connect)
        self.menu_File.addSeparator()
        self.menu_File.addAction(self.action_New_Project)
        self.menu_File.addAction(self.action_Open_Project)
        self.menu_File.addAction(self.action_Save_Project)
        self.menu_File.addSeparator()
        self.menu_File.addAction(self.actionE_xit)
        self.menu_Help.addAction(self.action_Context_Help)
        self.menu_Help.addAction(self.action_About)
        self.menubar.addAction(self.menu_File.menuAction())
        self.menubar.addAction(self.menu_Help.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "My 2 Ca - MySQL to Cassandra", None, QtGui.QApplication.UnicodeUTF8))
        self.connectButton.setText(QtGui.QApplication.translate("MainWindow", "Connect", None, QtGui.QApplication.UnicodeUTF8))
        self.codegenButton.setText(QtGui.QApplication.translate("MainWindow", "Generate", None, QtGui.QApplication.UnicodeUTF8))
        self.menu_File.setTitle(QtGui.QApplication.translate("MainWindow", "&File", None, QtGui.QApplication.UnicodeUTF8))
        self.menu_Help.setTitle(QtGui.QApplication.translate("MainWindow", "&Help", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Connect.setText(QtGui.QApplication.translate("MainWindow", "&Connect", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Save_Project.setText(QtGui.QApplication.translate("MainWindow", "&Save Project", None, QtGui.QApplication.UnicodeUTF8))
        self.action_New_Project.setText(QtGui.QApplication.translate("MainWindow", "&New Project", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Open_Project.setText(QtGui.QApplication.translate("MainWindow", "&Open Project", None, QtGui.QApplication.UnicodeUTF8))
        self.actionE_xit.setText(QtGui.QApplication.translate("MainWindow", "E&xit", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Context_Help.setText(QtGui.QApplication.translate("MainWindow", "&Context Help", None, QtGui.QApplication.UnicodeUTF8))
        self.action_About.setText(QtGui.QApplication.translate("MainWindow", "&About...", None, QtGui.QApplication.UnicodeUTF8))

