#!env python
__author__ = 'samiths'

##
## Single file implementation of MY2CA for easy deployment
##

## Imports
import mako
import mako.lookup
import datetime
import getpass
import os
import sys
import shutil
import re
import MySQLdb

###################################################################
## MySQL Connection Specific

class MySQLConnect:
    def connect(self, host, username, password, db, port):
        try:
            connection = MySQLdb.connect(host,username,password,db,port)
            return connection
        except MySQLdb.Error,e:
            print 'Error: Connection Failed to the server: %s' % (e.args[1])
            raise Exception(e.args[1])
        pass

    def get_table_list(self, connection):

        query = """SHOW TABLES;"""
        c = connection.cursor()
        c.execute(query)
        res = c.fetchall()
        res = list(r[0] for r in res)
        return res

    def get_table_info(self, connection, table):
        query = 'SHOW CREATE TABLE ' + str(table) + ';'
        c = connection.cursor()
        c.execute(query)
        res = c.fetchall()
        return res[0][1]
    pass

mysqlconnect = MySQLConnect()


###################################################################
## Language Parser Specific

class SQLCol:
    name = str()
    type = str()
    pytype = str()
    custype = str()
    typeargs = {}
    pytypeargs = str()
    indexed = False
    pk = False
    null = True
    fk_cf = None
    fk_col = None

    def __unicode__(self):
        return self.name + ":" + self.type

    def __str__(self):
        return self.__unicode__()

    pass

class SQLTable:
    name = str()
    cols = []
    pks = []
    engine = "InnoDB"
    dcharset = "utf8"

    pass

class SQLParse:

    def convert_sql_table(self, createsql):
        tbl = SQLTable()
        match = re.search(r'CREATE\s+TABLE\s+`(\w+)`\s*\(\s*(.*)\s*\)\s*ENGINE=(\w+)\s+DEFAULT\s+CHARSET=(\w+)\s*(COLLATE=\w+)?\s*(COMMENT=\'(.*)\')?\s*', createsql, re.DOTALL)
        if match:
            tbl.name = match.group(1)
            tbl.engine = match.group(3)
            tbl.dcharset = match.group(4)


            bodymatch = re.findall(r'\s*`(\w+)`\s+(\w+)(\((\d+)\))?[\s\w]*,*', match.group(2))
            keymatch = re.findall(r'\s+PRIMARY\s+KEY\s+\(`(\w+)`\),', match.group(2))
            cols = dict()
            for bm in bodymatch:
                col = SQLCol()
                col.indexed = False
                col.name = bm[0]
                col.type = bm[1]
                if bm[2]:
                    col.typeargs = bm[2]
                    pass
                cols[col.name] = col
                pass
            tbl.cols = cols.values()
            pass
        return tbl


    def generate_ca_query(self, token):
        pass


    def convert_sql(self, query):
        pass
    pass

lp = SQLParse()



###################################################################
## Code Generation Specific


author = 'Unknown'

'''
Template Lookup Directories and Include paths.
'''
template_lookup_dir = mako.lookup.TemplateLookup(directories=['templates', '/usr/local/share/my2ca/templates', '/usr/share/my2ca/templates',],
    module_directory='../.cache',
    output_encoding='utf-8')



def render_template(template, **args):
    '''
    Render the template file given by the <i>template</i> argument,
    using <i>args</i> as the data.
    '''
    t = template_lookup_dir.get_template(template)
    return t.render_unicode(**args)




def gen_module(modulename, outpath, data):
    '''
    Generate the module using master template given in <i>modulename</i>,
    using data in <i>data</i>,
    outputs to <i>outpath</i>
    '''
    ofile = open(outpath, 'w')
    if ofile == None:
        raise IOError("given path is not writable")
    if ofile.closed:
        raise IOError("file created but closed to access")
    ofile.write(render_template(modulename, data))
    ofile.flush()
    ofile.close()


# Output dir location
_output_dir = "../generated_code"

def _get_path(filename):
    return os.path.join(_output_dir,filename)

class CodeGen:
    """
    This keeps the CodeGen functions tight together
    """

    tables = {}
    selected_table = []

    keyspace = str()
    servers = str()
    credentials = str()

    connection = None

    def get_tables_structure(self):

        tbllist = []

        for tbl in mysqlconnect.get_table_list(self.connection):
            tbllist.append((tbl,lp.convert_sql_table((mysqlconnect.get_table_info(self.connection, tbl)))))
            pass
        self.tables = dict(tbllist)
        pass

    def export_ca_model(self):

        return render_template("model.cql",
            author = _get_author(),
            date=_get_date(),
            keyspace = self.keyspace,
            t = self.selected_table
        )

    def select_table(self, table):
        tabledef = self.tables.get(table)
        self.selected_table.append(tabledef)
        pass

    def deselect_table(self, table):
        self.selected_table.remove(table)
        pass

    def generate_code(self):
        """
        Generate code for the selected tables
        """

        if os.path.exists(_output_dir):
            #if the dir exists removes the existing files/folders
            shutil.rmtree(_output_dir)
            pass

        #create folder
        os.makedirs(_output_dir)

        f = open(_get_path("conpool.py"),"w")

        f.write(render_template("conpool.py",
            author = _get_author(),
            date=_get_date(),
            keyspace = self.keyspace,
            servers = self.servers,
            credentials = self.credentials))
        f.flush()
        f.close()

        f = open(_get_path("structure.cql"),"w")

        f.write(self.export_ca_model())
        f.flush()
        f.close()

        f = open(_get_path("entity.py"),"w")

        f.write(render_template("entity.py",
            author = _get_author(),
            date=_get_date()))
        f.flush()
        f.close()

        for ff in self.selected_table:
            print "Generating Table : " + ff.name
            f = open(_get_path(ff.name + ".py"),"w")
            f.write(self.generate_table(ff))
            f.flush()
            f.close()
            pass
        pass

    def select_all(self):
        self.selected_table = self.tables.values()
        pass

    def generate_table_by_name(self, table_name):
        content = self.tables.get(table_name)
        return render_template("entitytemplate.py", author = _get_author(), date = _get_date(), t = content)

    def generate_table(self, table):
        return render_template("entitytemplate.py", author = _get_author(), date = _get_date(), t = table)
    pass

codegen = CodeGen()

def _get_author():
    return getpass.getuser()

def _get_date():
    return datetime.date.today()

###################################################################


###################################################################
## UI Genered Content
from uigen import *
###################################################################

###################################################################
## UI related classes

from PySide.QtGui import *

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
        codegen.get_tables_structure()
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



class ConnectMySqlDlg(QDialog):

    def __init__(self, parent = None):
        QDialog.__init__(self, parent)
        self.ui = Ui_connectMySqlDlg()
        self.ui.setupUi(self)

    def run(self):
        self.exec_()

    def get_details(self):

        """Validate"""

        host = self.ui.hostE.text()
        if host == "":
            raise Exception('Host cannot be empty')

        user = self.ui.userE.text()
        if user=="":
            raise Exception('User cannot be empty')

        database = self.ui.dbE.text()
        if database=="":
            raise Exception('Database name cannot be empty')

        details = {'host':host,
                   'user':self.ui.userE.text(),
                   'password':self.ui.passE.text(),
                   'database':self.ui.dbE.text(),
                   'port':self.ui.portE.text(),}
        return details




class MainWindow(QMainWindow):

    connection = None

    messageBox = None

    def generate_code(self):
        if self.connection == None:
            print "Generate Code: No connection to generate code"
            pass
        connection = self.connection
        wiz = CodegenWiz(self)
        wiz.run()
#        codegen.select_all()
#        codegen.generate_code()
#        docgen.generate_doc()
#        QMessageBox.information(self,"Generate","Generation Succesful")
        pass

    def generate_doc(self):
        pass

    def test_code(self):
        pass

    def connect_mysql(self):
        dlg = ConnectMySqlDlg()
        dlg.run()
        if dlg.result():
            try:
                c = dlg.get_details()
            except Exception as e:
                QMessageBox.critical(self,"Open MySQL", e.message)
                return


            try:

                self.connection = mysqlconnect.connect(c['host'],
                    c['user'],
                    c['password'],
                    c['database'],
                    int(c['port']))
            except Exception as e:
                QMessageBox.critical(self, "Open MySQL", e.message)
                return

            self.tablelist = mysqlconnect.get_table_list(self.connection)
            model = QStringListModel()
            model.setStringList(self.tablelist)
            self.ui.tablesList.setModel(model)
            codegen.connection = self.connection
            codegen.keyspace = c['database']
            codegen.get_tables_structure()


    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.connectButton.clicked.connect(self.connect_mysql)
        self.ui.codegenButton.clicked.connect(self.generate_code)
        self.messageBox = QMessageBox(self)

    def run(self):
        self.show()


###################################################################

class My2Ca:

    def cmd_handle_main(self):
        if len(sys.argv) < 2:
            # No arguments passed. lets print the usage and exit
            self.cmd_print_usage()
            exit(0)
            pass
        arg = sys.argv[1]


        if arg == '-g':
            '''GUI application requested'''
            from PySide import QtGui
            app = QtGui.QApplication(sys.argv)
            mw = MainWindow()
            mw.run()
            sys.exit(app.exec_())
            pass

        if arg == '-h':
            self.cmd_print_usage()
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
            else:
                c_password = ""
                pass

            from my2ca.mysqlcon.mysqlconmanager import connect

            connection = connect(c_host, c_user, c_password, c_db, c_port)

            from my2ca.codegen.codegen import codegen

            codegen.connection = connection
            codegen.keyspace = c_db
            codegen.get_tables_structure()
            codegen.select_all()
            codegen.export_ca_model()
            codegen.generate_code()

            from my2ca.docgen import docgen
            docgen.generate_doc()
        pass

    def cmd_print_usage(self):
        print "my2ca [-g|-h|gen]"
        print "\t-g\tOpen the GUI"
        print "\t-h\tShow this help"
        print "\tgen [host][port][database][user][password]"
        print "\t\tGenerate the PyCassa code for given database"
        pass
    pass

my2ca = My2Ca()


if __name__ == '__main__':
    my2ca.cmd_handle_main()
    pass
