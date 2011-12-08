'''
Created on Oct 31, 2011

@author: sam
'''

from PySide.QtGui import *
from PySide.QtCore import *

from my2ca.codegen.codegen import codegen

from my2ca.mysqlcon import mysqlconmanager

from my2ca.ui.ui_select_tables_page import Ui_selectTablesPage
from my2ca.ui.ui_preview_page import Ui_previewPage


connection = None
available_tables = None
selected_tables = None


class SelectTablesPage(QWizardPage):
    
    def __init__(self):
        QWizardPage.__init__(self)
        self.ui = Ui_selectTablesPage()
        self.ui.setupUi(self)
        
        self.ui.addButton.clicked.connect(self.add)
        self.ui.addAllButton.clicked.connect(self.addAll)
        self.ui.removeButton.clicked.connect(self.remove)
        self.ui.removeAllButton.clicked.connect(self.removeAll)
        
        model = QStringListModel()
        model.setStringList(codegen.tables.values())
        #self.ui.availableTableList.setModel(model)
        pass
    
    def add(self):
        codegen.select_table(self.ui.availableTableList.selectedItems()[0][0])
        pass
    
    def addAll(self):
        codegen.select_table(codegen.tables.values())
        pass
    
    def remove(self):
        pass
    
    def removeAll(self):
        pass
    
    pass

class PreviewCodePage(QWizardPage):
    
    def __init__(self):
        QWizardPage.__init__(self)
        self.ui = Ui_previewPage()
        self.ui.setupUi(self)
        self.ui.outputFilesList.itemSelectionChanged.connect(self.on_selectedfile_changed)
        pass
    
    def on_selectedfile_changed(self):
        print "HI"
        pass
    
    pass

class ProgressPage(QWizardPage):
    
    def __init__(self):
        QWizardPage.__init__(self)
        pass
    
    pass

class FinalizePage(QWizardPage):
    
    def __init__(self):
        QWizardPage.__init__(self)
        pass
    
    pass

class CodegenWiz(QWizard):
    
    def run(self):
        self.exec_()
        pass
    
    def __init__(self, parent = None):
        QWizard.__init__(self, parent)
        
        self.selectTablePage = SelectTablesPage()
        self.previewCodePage = PreviewCodePage()
        self.progressPage = ProgressPage()
        self.finalizePage = FinalizePage()
        
        self.addPage(self.selectTablePage)
        self.addPage(self.previewCodePage)
        self.addPage(self.progressPage)
        self.addPage(self.finalizePage)
        
        self.setWindowTitle('Generate Code')
        
        pass
    
    pass
