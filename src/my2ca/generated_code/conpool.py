'''
Auto Generated by my2ca
@author: sam
Generated on 2011-11-29
'''

import pycassa

'''
Please use another mechanism to handle these data
'''
keyspace = ""
servers = 
credentials = 

"""
The Connection Pool
"""
connection_pool = pycassa.connect(keyspace=keyspace, servers=servers, credentials=credentials)
