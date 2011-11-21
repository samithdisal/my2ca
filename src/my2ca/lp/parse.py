'''
Created on Oct 31, 2011

@author: sam
'''

#sqlparse do not supports CREATE statements yet.
from pyparsing import *

import sqlparse
from sqlparse.tokens import DML


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


def _strip(s,loc,tok):
    res = str()
    for c in tok[0]:
        if c != "`":
            res += c
            pass
        pass
    return res

def convert_sql_table(createsql):
    tbl = SQLTable()
    
    paranths = Forward()
    paranths << "(" + ZeroOrMore(CharsNotIn("()") | paranths) + ")"
    
    idt = Word("`",alphanums + "`").setName("simple_identifier")
    
    idt.addParseAction(_strip)
    
    pk_def = Group(Literal("PRIMARY") + "KEY" + "(" + delimitedList(idt).setResultsName("pks") + ")")
    
    key_def = Group(Literal("KEY") + idt.setResultsName("key_id") + "(" + idt.setResultsName("key_name") + ")" ).setResultsName("key")
    
    key_list_def = Group(delimitedList(key_def, ","))
    
    constraint_def = Group(Literal("CONSTRAINT") + idt.setResultsName("constraint_id") + "FORIEGN" + "KEY"
                           + "(" + idt.setResultsName("foriegn_key") + "REFERENCES" + idt.setResultsName("ref_table") 
                           + "(" + idt.setResultsName("ref_table_field") + ")").setResultsName("constraint")
    
    constraint_list_def = Group(delimitedList(constraint_def, ","))
    
    field_def = Group(idt.setResultsName("fieldname") + Word(alphas).setResultsName("fieldtype") 
                      + Optional(paranths) + Optional(Literal("NOT") + "NULL") + Optional(Literal("DEFAULT") + "NULL") + Optional(Literal("AUTO_INCREMENT"))).setResultsName("field")
    
    field_list_def = Group(delimitedList(field_def, ","))
    
    
    
    create_table_def = (Literal("CREATE") + "TABLE" + idt.setResultsName("tablename") 
                        + "(" + field_list_def.setResultsName("fields") + "," + pk_def.setResultsName("pks")
                        + Optional("," + key_list_def.setResultsName("keys") + "," + constraint_list_def.setResultsName("constraints"))
                        + ")" + ZeroOrMore(Word(alphanums + "=")))
    
    tokens = create_table_def.parseString(createsql)
    
    tbl.name = tokens.tablename
    
    print tokens.tablename
    for f in tokens.fields:
        fil = SQLCol()
        fil.name = f.fieldname
        fil.type = f.fieldtype
        tbl.cols.append(fil)
        print f.fieldname, " => ", f.fieldtype
        pass
    
    tbl.pks = tokens.pks
    print tbl.pks.pks
    
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
    convert_sql_table("""CREATE TABLE `SaleTransaction` (`id` bigint(20) NOT NULL AUTO_INCREMENT,`amount` bigint(20) DEFAULT NULL,`datetime` date NOT NULL, `acount_accountId` varchar(255) DEFAULT NULL,`cd_id` bigint(20) DEFAULT NULL,`customer_customerId` varchar(255) DEFAULT NULL,PRIMARY KEY (`id`),KEY `FK42944FF76AED1F08` (`acount_accountId`),KEY `FK42944FF7ED21FE54` (`customer_customerId`),KEY `FK42944FF7A990C8F6` (`cd_id`),CONSTRAINT `FK42944FF76AED1F08` FOREIGN KEY (`acount_accountId`) REFERENCES `Account` (`accountId`),CONSTRAINT `FK42944FF7A990C8F6` FOREIGN KEY (`cd_id`) REFERENCES `CD` (`id`),CONSTRAINT `FK42944FF7ED21FE54` FOREIGN KEY (`customer_customerId`) REFERENCES `Customer` (`customerId`)) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8""")