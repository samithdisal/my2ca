'''
Created on Aug 14, 2011

@author: sam
'''

if __name__ == '__main__':
    
    import sys
    for arg in sys.argv:
        if arg == '-g':
            '''GUI application requested'''
            from PySide import QtGui
            from ui import major
            app = QtGui.QApplication(sys.argv)
            mw = major.MainWindow()
            mw.ui.show()
            sys.exit(app.exec_())