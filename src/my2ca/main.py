'''
Created on Aug 14, 2011

@author: sam
'''

def _print_usage():
    
    print "my2ca [-g|-h|gen]"
    print "\t-g\tOpen the GUI"
    print "\t-h\tShow this help"
    print "\tgen [host][port][database][user][password]"
    print "\t\tGenerate the PyCassa code for given database"
    pass


if __name__ == '__main__':
    
    import sys
    
    arg = sys.argv[1]
    
    
    if arg == '-g':
        '''GUI application requested'''
        from PySide import QtGui
        from ui import major
        app = QtGui.QApplication(sys.argv)
        mw = major.MainWindow()
        mw.run()
        sys.exit(app.exec_())
        pass
    
    if arg == '-h':
        _print_usage()
        pass
    
    if arg == 'gen':
        """
        Generate Code for the given address
        """
        
        c_host = sys.argv[2]
        c_port = int(sys.argv[3])
        c_db = sys.argv[4]
        c_user = sys.argv[5]
        if len(sys.argv) == 7:
            c_password = sys.argv[6]
            pass
        
        from my2ca.mysqlcon.mysqlconmanager import connect
        
        connection = connect(c_host, c_user, c_password, c_db, c_port)
        
        from my2ca.codegen.codegen import codegen
        
        codegen.connection = connection
        codegen.keyspace = c_db;
        codegen.get_tables_structure()
        codegen.select_all()
        codegen.export_ca_model()
        codegen.generate_code()
        
        from my2ca.docgen import docgen
        docgen.generate_doc()
        pass
    pass
        