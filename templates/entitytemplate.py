
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

class ${t.name}(entity):
    """
    ${t.name} data entity class
    """
    
    __ca_cf = "${t.name}"
    __ca_hash = None
    
    % for col in t.cols:
    ${makecol(col)}
    % endfor
    def __init__(self):
        entity.__init__(self)
    
    ${makeinsert(t.cols)}
    ${makeremove()}
    
<%def name="makecol(col)">
    
    """ Column ${col.name} """
    % if col.fk:
    _${col.name} = None
    % elseif:
    _${col.name} = ${col.pytype}(${col.pytypeargs})
    % endif
    
    def set_${col.name}(self, value):
        """
        Set ${col.name} value to 'value'
        """
        % if col.fk:
        self._${col.name} = value.__ca_hash
        % else:
        self._${col.name} = value
        % endif
        pass
    
    def get_${col.name}(self):
        """
        Get ${col.name} value
        """
        % if col.fk:
        temp = ${col.name}.get(self.${col.name})
        % else:
        return self._${col.name}
        % endif
    
    % if col.indexed:
    @classmethod
    def find_by_${col.name}(val):
        ${col.name}_expr = pycassa.create_index_expression('${col.name}', val)
        clause = pycassa.create_index_clause([${col.name}_expr])
        result = users.get_indexed_slices(clause)
        result_list = list(${col.name}.get(f[' for f in result)
        return 
    % endif
</%def>

<%def name="makeinsert(cols)">
    
    def persist(self):
        """
        Default Insert/Update Method Call this after an update or after creating an object
        """
        if self.__ca_hash == None:
            self.__ca_hash == uuid.uuid4()
            #triggers specially for pre insert
            #---------------------
            
            #---------------------
        else:
            #triggers specially for non inserting pre update
            #---------------------
            
            #---------------------
        
        cf = pycassa.ColumnFamily(conpool.connection_pool, self.__ca_cf)
        
        #triggers for pre insert or update
        #-------------------------
        
        #-------------------------
        
        cf.insert(
                  self.__ca_hash,
                  {
                   % for col in cols:
                   '${col.name}': self.${col.name},
                   % endfor
                   }
                  )
        
        #triggers for post insert or update
        #-------------------------
        
        #-------------------------
        pass
    
</%def>
<%def name="makeremove()">
    
    def remove(self):
        """
        Default Remove Method
        """
        if self.__ca_hash == None:
            #the object is not persisted so nothing to remove anyway
            return False
        cf = pycassa.ColumnFamily(conpool.connection_pool, self.__ca_cf)
        
        #triggers for pre remove
        #---------------------------
        
        #---------------------------
        
        cf.remove(self.__ca_hash)
        
        #tridders for post remove
        #---------------------------
        
        #---------------------------
        return True
    
</%def>
<%def name="construct(t)">
    
    def __init__(self):
        """
        Default Constructor Method
        """
        pass
    
</%def>
<%def name="get(t)">
    
    @classmethod
    def get(id):
        """
        Get by hashcode
        """
        cf = pycassa.ColumnFamily(conpool.connection_pool, self.__ca_cf)
        res = cf.get(id)
        
        t = ${t.name}()
        t.__ca_hash = id
        
        % for c in t.cols:
            t.set_${c.name}(res.get(${c.name}))
        % endfor
        
        return t
    
</%def>