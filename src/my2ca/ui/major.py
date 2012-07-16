'''
Created on Aug 14, 2011

@author: sam
'''
from PySide.QtGui import *
from PySide.QtCore import *
from PySide import QtUiTools
from my2ca.mysqlcon import mysqlconmanager
from my2ca.ui import ui_mainwindow, codegen_wiz, ui_connectMySqlDlg
from my2ca.codegen.codegen import codegen, CodeGen
from my2ca.docgen import docgen

class ConnectMySqlDlg(QDialog):
    
    def __init__(self, parent = None):
        QDialog.__init__(self, parent)
        self.ui = ui_connectMySqlDlg.Ui_connectMySqlDlg()
        self.ui.setupUi(self)
    
    def run(self):
        self.exec_()
    
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
        if self.connection == None:
            pass
#        codegen_wiz.connection = self.connection
#        wiz = codegen_wiz.CodegenWiz(self)
#        wiz.run()
        
        codegen.select_all()
        codegen.generate_code()
        docgen.generate_doc()
        QMessageBox.information(self,"Generate","Generation Succesful")
        pass
    
    def generate_doc(self):
        pass
    
    def test_code(self):
        pass
    
    def connect_mysql(self):
        dlg = ConnectMySqlDlg()
        dlg.run()
        if dlg.result():
            c = dlg.get_details()
            self.connection = mysqlconmanager.connect(c['host'],
                                                      c['user'],
                                                      c['password'],
                                                      c['database'],
                                                      int(c['port']))
            if self.connection == None:
                QMessageBox.warning(self, "Connect to Database","Connection Failed")
                return
            self.tablelist = mysqlconmanager.get_table_list(self.connection)
            model = QStringListModel()
            model.setStringList(self.tablelist)
            self.ui.tablesList.setModel(model)
            codegen.connection = self.connection
            codegen.keyspace = c['database']
            codegen.get_tables_structure()


    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = ui_mainwindow.Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.connectButton.clicked.connect(self.connect_mysql)
        self.ui.codegenButton.clicked.connect(self.generate_code)
    
    def run(self):
        self.show()