'''
Created on Nov 18, 2011

@author: sam
'''

from my2ca.codegen.templating import render_template
from my2ca.lp.parse import convert_sql_table
from my2ca.mysqlcon import mysqlconmanager
from my2ca.mysqlcon.mysqlconmanager import get_table_list, get_table_info
import datetime
import getpass
import os
import shutil


# Output dir location
_output_dir = "generated_code"

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
        
        for tbl in get_table_list(self.connection):
            tbllist.append((tbl,convert_sql_table((get_table_info(self.connection, tbl)))))
            pass
        self.tables = dict(tbllist)
        print self.tables
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

if __name__ == '__main__':
    codegen.connection = mysqlconmanager.connect("localhost", "root", "123", "test", 3306)
    codegen.get_tables_structure()
    codegen.select_table("Test")
    codegen.generate_code()
    