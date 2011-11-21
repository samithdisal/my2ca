'''
Created on Nov 18, 2011

@author: sam
'''

from my2ca.lp.parse import convert_sql_table, generate_ca_query, SQLTable
from my2ca.mysqlcon.mysqlconmanager import get_table_list, get_table_info

import os, sys
from my2ca.codegen.templating import render_template

class CodeGen:
    """
    This keeps the CodeGen functions tight together
    """
    
    tables = {}
    selected_table = []
    
    connection = None
    
    def get_tables_structure(self):
        
        tbllist = []
        
        for tbl, in get_table_list(self.connection):
            tbllist.append((tbl,convert_sql_table((get_table_info(self.connection, tbl)))))
            pass
        self.tables = dict(tbllist)
        print self.tables
        pass
    
    def export_ca_model(self):
        pass
    
    def generate_table(self, table_name):
        print table_name
        content = self.tables.get(table_name)
        print render_template("entitytemplate.py", author = "NoAuthor", date = "nodate", t = content)
    pass

codegen = CodeGen()
    
    