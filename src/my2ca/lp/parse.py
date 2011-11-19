'''
Created on Oct 31, 2011

@author: sam
'''

#sqlparse do not supports CREATE statements yet.
from pyparsing import *
import string



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
    cols = []
    pks = []
    engine = "InnoDB"
    dcharset = "utf8"
    
    pass

def tokenize(statement):
    return statement.tokens


def _get_columns(toks):
    pass

def convert_table(createsql):
    
    tbl = SQLTable()
    
    createTableStmt = Forward()
    createToken = Keyword("create", caseless=True)
    tableToken = Keyword("table", caseless=True)
    
    primarykeyToken = Keyword("primary key", caseless=True)
    engineToken = Keyword("engine", caseless=True)
    charsetToken = Keyword("default charset", caseless=True)
    
    EQU_ = Keyword("=")
    NOTNULL_ = Keyword("not null", caseless=True)
    DEFNULL_ = Keyword("default null", caseless=True)
    
    
    
    #starts with a letter and then any alphanumeric charactor
    ident = Word("`" + alphas + "`").setName("identifier")
    valtype = Word(alphas).setName("valtype")
    numbers = Word(alphanums).setName("numbers")
    
    tablename = Upcase(ident)
    
    columnStmt = Forward()
    
    
    columnName = Upcase(ident)
    columnType = Upcase(valtype+Optional(Literal("(")+numbers+Literal(")"),""))
    
    columnStmt << columnName + columnType + (NOTNULL_ | DEFNULL_ ) + Literal(",")
    
    columnList = Group(OneOrMore(columnStmt.setResultsName("column", True)))
    
    primary_key = Forward()
    
    a_primary_key = Upcase(ident)
    primary_key << Literal("(").suppress() + a_primary_key + ZeroOrMore(Literal(",") + a_primary_key) + Literal(")").suppress()
    
    engine = ident
    
    charset = ident
    
    
    createTableStmt << ( createToken + tableToken + tablename.setResultsName("tablename") + Literal("(") + columnList.setResultsName("columns") + ZeroOrMore( ident + Literal(","))
                        + primarykeyToken + primary_key.setResultsName("pk") + Literal(")"))
    
    tokens = createTableStmt.parseString(createsql)
    
    tbl.name = tokens.tablename
    tbl.pks = tokens.pk
    tbl.cols = tokens.columns
    
    return tbl

def generate_ca_query(token):
    pass
                        

if __name__ == '__main__':
    convert_table("""CREATE TABLE `Category` ( `categoryId` bigint(20) NOT NULL, `categoryName` varchar(255) DEFAULT NULL, PRIMARY KEY (`categoryId`) ) ENGINE=InnoDB DEFAULT CHARSET=utf8""")