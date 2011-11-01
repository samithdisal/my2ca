'''
Created on Oct 31, 2011

@author: sam
'''
import sqlparse
from sqlparse import tokens, filters, sql

class SQLCol:
    name = str()
    type = str()
    typeargs = {}
    indexed = False
    pk = False
    null = True
    
    pass

class SQLTable:
    name = str()
    cols = {}
    pks = {}
    engine = "InnoDB"
    dcharset = "utf8"
    
    pass

def tokenize(statement):
    return statement.tokens

def parsesql(query):
    res = sqlparse.parse(query)
    return res

def _get_columns(toks):
    pass

def convert_table(createsql):
    res = parsesql(createsql)
    r = res[0]
    if r.get_type() != "CREATE":
        return False
    toks = tokenize(res[0])
    
    tbl = SQLTable()
    
    for t in toks:
        if t.is_whitespace():
            continue
        if isinstance(t, sql.Function):
            ftoks = t.tokens
            for ft in ftoks:
                if isinstance(ft, sql.Identifier):
                    if ft.tokens[0].value == "ENGINE":
                        continue
                    tbl.name = ft.tokens[0].value
                if isinstance(ft,sql.Parenthesis):
                    tbl.cols =_get_columns(ft.tokens)
                    pass
                pass
            pass
        print "<token>" + str(t) + "</token>"
    pass

def generate_ca_query(token):
    pass

if __name__ == '__main__':
    convert_table("""CREATE TABLE `authors` (
                  `username` varchar(45) NOT NULL,
                  `displayname` varchar(45) NOT NULL,
                  `password` varchar(45) NOT NULL,
                  `activities` int(11) NOT NULL,
                  `registerdate` datetime NOT NULL,
                  `lastlogin` datetime NOT NULL,
                  PRIMARY KEY (`username`)
                ) ENGINE=InnoDB DEFAULT CHARSET=utf8"""
                  )