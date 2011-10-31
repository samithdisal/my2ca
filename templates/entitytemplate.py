
'''
Auto Generated by my2ca
@author: ${author}
Generated on ${date}
'''

import pycassa
import uuid
import pickle

import conpool

from entity import entity

class ${entity_name}(entity):
    """
    ${entity_name} data entity class
    """
    
    __ca_cf = "${entity_name}"
    __ca_cf = 
    
    % for col in cols:
    ${makecol(col)}
    % endfor
    def __init__(self):
        entity.__init__(self)
    
    ${makeinsert(cols)}
    
<%def name="makecol(col)">
    self.${col.name} = ${col.datatype}(${col.typeargs})
</%def>
<%def name="makeinsert(cols)">
    """
    Default Insert/Update Method
    """
    def persist(self):
        if self.__ca_hash == None:
            self.__ca_hash == uuid.uuid4()
        cf = pycassa.ColumnFamily(conpool.connection_pool, self.__ca_cf)
        cf.insert(
                  self.__ca_hash,
                  {
                   % for col in cols:
                   '${col.name}': self.${col.name},
                   % endfor
                   }
                  )
        pass
</%def>
<%def name="makeremove(cols)">
    """
    Default Remove Method
    """
    def remove(self):
        if self.__ca_hash == None:
            #the object is not persisted so nothing to remove anyway
            return False
        cf = pycassa.ColumnFamily(conpool.connection_pool, self.__ca_cf)
        cf.remove(self.__ca_hash)
        return True
</%def>