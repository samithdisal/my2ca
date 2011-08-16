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
    connection.query(query)
    rows = connection.store_results().fetchall()
    return rows
