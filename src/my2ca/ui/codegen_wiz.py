'''
Created on Oct 31, 2011

@author: sam
'''

from PySide.QtGui import *

class SelectTablesPage(QWizardPage):
    
    def __init__(self):
        QWizardPage.__init__(self)
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
