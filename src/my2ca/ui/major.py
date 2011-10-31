'''
Created on Aug 14, 2011

@author: sam
'''
from PySide.QtGui import *
from PySide.QtCore import *
from PySide import QtUiTools
from my2ca.mysqlcon import mysqlconmanager
from my2ca.ui import ui_mainwindow

class ConnectMySqlDlg:
    
    def __init__(self):
        self.ui = QtUiTools.QUiLoader().load('ui/uic/connectMySqlDlg.ui', None)
    
    def run(self):
        self.ui.exec_()
    
    def get_details(self):
        details = {'host':self.ui.hostE.text(),
                   'user':self.ui.userE.text(),
                   'password':self.ui.passE.text(),
                   'database':self.ui.dbE.text(),
                   'port':self.ui.portE.text(),}
        return details;




class MainWindow(QMainWindow):
    
    connection = None
    
    def generate_code(self):
        pass
    
    def generate_doc(self):
        pass
    
    def test_code(self):
        pass
    
    def connect_mysql(self):
        dlg = ConnectMySqlDlg()
        dlg.run()
        if dlg.ui.result():
            c = dlg.get_details()
            self.connection = mysqlconmanager.connect(c['host'],
                                                      c['user'],
                                                      c['password'],
                                                      c['database'],
                                                      int(c['port']))
            self.tablelist = mysqlconmanager.get_table_list(self.connection)
            model = QStringListModel()
            strings = list( tbl[0] for tbl in self.tablelist )
            model.setStringList(strings)
            self.ui.tablesList.setModel(model)
    
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = ui_mainwindow.Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.connectButton.clicked.connect(self.connect_mysql)
    
    def run(self):
        self.show()