'''
Created on Oct 31, 2011

@author: sam
'''
import sqlparse

def torkanize(query):
    res = sqlparse.parse(query)
    return res

def generate_ca_query(token):
    pass
