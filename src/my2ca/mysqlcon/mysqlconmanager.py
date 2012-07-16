'''
Created on Aug 15, 2011

@author: sam
'''

import MySQLdb

def connect(host, username, password, db, port):
    try:
        connection = MySQLdb.connect(host,username,password,db,port)
        return connection
    except MySQLdb.Error,e:
        print "Error: Connection Failed to the server: %s" % (e.args[1])
        return None

def get_table_list(connection):
    
    query = """SHOW TABLES;"""
    c = connection.cursor()
    c.execute(query)
    res = c.fetchall()
    res = list(r[0] for r in res)
    print res
    return res

def get_table_info(connection, table):
    query = 'SHOW CREATE TABLE ' + str(table) + ';'
    c = connection.cursor()
    c.execute(query)
    res = c.fetchall()
    return res[0][1]