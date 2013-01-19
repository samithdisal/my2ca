'''
Created on Oct 31, 2011

@author: sam
'''

#sqlparse do not supports CREATE statements yet.
from pyparsing import *

import sqlparse
from sqlparse.tokens import DML

# Regular expression library
import re


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
        return self.name + ":" + self.type + ":" + self.typeargs

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

def tokenize(statement):
    return statement.tokens


def _strip(s,loc,tok):
    res = str()
    for c in tok[0]:
        if c != "`":
            res += c
            pass
        pass
    return res

def convert_sql_table(createsql):
    
    #print createsql
    tbl = SQLTable()

    id_lit = r'`[a-z][A-Z][0-9]_'
    match = re.search(r'CREATE\s+TABLE\s+`(\w+)`\s*\(\s*(.*)\s*\)\s*ENGINE=(\w+)\s+DEFAULT\s+CHARSET=(\w+)\s*', createsql)
    if match:
        print match.group()
        print 'Table Name is '+match.group(1)
        print 'Body is ' + match.group(2)
        print 'Engine is ' + match.group(3)
        print 'Char Set is ' + match.group(4)

        bodymatch = re.findall(r'\s*`(\w+)`\s+(\w+)(\((\d+)\))?[\s\w]*,*', match.group(2))
        keymatch = re.findall(r'\s+PRIMARY\s+KEY\s+\(`(\w+)`\),', match.group(2))
        print bodymatch
        print keymatch
        cols = dict()
        for bm in bodymatch:
            col = SQLCol()
            col.name = bm[0]
            col.type = bm[1]
            if bm[2]:
                col.typeargs = bm[2]
                pass
            print col
            pass
        pass
    return tbl


def generate_ca_query(token):
    pass


def convert_sql(query):
    stmts = sqlparse.parse(query)
    for s in stmts:
        if s.tokens[0].type == DML:
            print "Hmmm"
        pass
    pass



if __name__ == '__main__':
    convert_sql_table("""CREATE TABLE `Account` ( `accountId` varchar(255) NOT NULL, `balance` bigint(20) NOT NULL, `customer_customerId` varchar(255) DEFAULT NULL, PRIMARY KEY (`accountId`), KEY `FK1D0C220DED21FE54` (`customer_customerId`), CONSTRAINT `FK1D0C220DED21FE54` FOREIGN KEY (`customer_customerId`) REFERENCES `Customer` (`customerId`) ) ENGINE=InnoDB DEFAULT CHARSET=utf8""")