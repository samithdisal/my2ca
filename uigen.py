# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created: Tue Feb 12 12:43:47 2013
#      by: pyside-uic 0.2.13 running on PySide 1.1.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 599)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
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
        self.verticalLayout.addWidget(self.widget)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.tablesList = QtGui.QListView(self.centralwidget)
        self.tablesList.setObjectName("tablesList")
        self.horizontalLayout.addWidget(self.tablesList)
        self.erdArea = QtGui.QScrollArea(self.centralwidget)
        self.erdArea.setWidgetResizable(True)
        self.erdArea.setObjectName("erdArea")
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 387, 509))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.erdArea.setWidget(self.scrollAreaWidgetContents)
        self.horizontalLayout.addWidget(self.erdArea)
        self.verticalLayout.addLayout(self.horizontalLayout)
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

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'connectMySqlDlg.ui'
#
# Created: Tue Feb 12 12:43:48 2013
#      by: pyside-uic 0.2.13 running on PySide 1.1.1
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

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'select_tables_page.ui'
#
# Created: Tue Feb 12 12:43:48 2013
#      by: pyside-uic 0.2.13 running on PySide 1.1.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_selectTablesPage(object):
    def setupUi(self, selectTablesPage):
        selectTablesPage.setObjectName("selectTablesPage")
        selectTablesPage.resize(653, 399)
        self.horizontalLayout = QtGui.QHBoxLayout(selectTablesPage)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.availableTableList = QtGui.QListView(selectTablesPage)
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
        self.selectedTableList = QtGui.QListView(selectTablesPage)
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

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'preview_page.ui'
#
# Created: Tue Feb 12 12:43:48 2013
#      by: pyside-uic 0.2.13 running on PySide 1.1.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_previewPage(object):
    def setupUi(self, previewPage):
        previewPage.setObjectName("previewPage")
        previewPage.resize(746, 525)
        self.horizontalLayout = QtGui.QHBoxLayout(previewPage)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.outputFilesList = QtGui.QListWidget(previewPage)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.outputFilesList.sizePolicy().hasHeightForWidth())
        self.outputFilesList.setSizePolicy(sizePolicy)
        self.outputFilesList.setObjectName("outputFilesList")
        self.horizontalLayout.addWidget(self.outputFilesList)
        self.previewText = QtGui.QTextBrowser(previewPage)
        self.previewText.setObjectName("previewText")
        self.horizontalLayout.addWidget(self.previewText)

        self.retranslateUi(previewPage)
        QtCore.QMetaObject.connectSlotsByName(previewPage)

    def retranslateUi(self, previewPage):
        previewPage.setWindowTitle(QtGui.QApplication.translate("previewPage", "Form", None, QtGui.QApplication.UnicodeUTF8))

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'progress_page.ui'
#
# Created: Tue Feb 12 12:43:48 2013
#      by: pyside-uic 0.2.13 running on PySide 1.1.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_progressPage(object):
    def setupUi(self, progressPage):
        progressPage.setObjectName("progressPage")
        progressPage.resize(400, 300)
        self.verticalLayout = QtGui.QVBoxLayout(progressPage)
        self.verticalLayout.setObjectName("verticalLayout")
        self.generateButton = QtGui.QPushButton(progressPage)
        self.generateButton.setObjectName("generateButton")
        self.verticalLayout.addWidget(self.generateButton)
        self.generateLog = QtGui.QTextEdit(progressPage)
        self.generateLog.setObjectName("generateLog")
        self.verticalLayout.addWidget(self.generateLog)

        self.retranslateUi(progressPage)
        QtCore.QMetaObject.connectSlotsByName(progressPage)

    def retranslateUi(self, progressPage):
        progressPage.setWindowTitle(QtGui.QApplication.translate("progressPage", "WizardPage", None, QtGui.QApplication.UnicodeUTF8))
        self.generateButton.setText(QtGui.QApplication.translate("progressPage", "Generate", None, QtGui.QApplication.UnicodeUTF8))

