'''
Created on Oct 31, 2011

@author: sam
'''

from PySide.QtGui import *

from my2ca.ui.ui_select_tables_page import Ui_selectTablesPage

class SelectTablesPage(QWizardPage):
    
    def __init__(self):
        QWizardPage.__init__(self)
        self.ui = Ui_selectTablesPage()
        self.ui.setupUi(self)
        
        self.ui.addButton.clicked.connect(self.add)
        self.ui.addAllButton.clicked.connect(self.addAll)
        self.ui.removeButton.clicked.connect(self.remove)
        self.ui.removeAllButton.clicked.connect(self.removeAll)
        pass
    
    def add(self):
        pass
    
    def addAll(self):
        pass
    
    def remove(self):
        pass
    
    def removeAll(self):
        pass
    
    pass

class PreviewCodePage(QWizardPage):
    
    def __init__(self):
        QWizardPage.__init__(self)
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
