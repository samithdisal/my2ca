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
    pytype = str()
    custype = str()
    typeargs = {}
    pytypeargs = str()
    indexed = False
    pk = False
    null = True
    fk_cf = None
    fk_col = None
    
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
        pass
    
    field_dict = dict(list((f.name,f) for f in tbl.cols))
    
    for c in tokens.constraints:
        field_dict.get(c.foriegn_key).indexed = True
        field_dict.get(c.foriegn_key).fk_cf = c.ref_table
        field_dict.get(c.foriegn_key).fk_field = c.ref_table_field
        pass
    
    for k in tokens.pks.pks:
        field_dict.get(k).pk = True
        pass
    
    tbl.pks = tokens.pks
    
    tbl.cols = field_dict.values()
    
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
    convert_sql_table("""""")