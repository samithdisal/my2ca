'''
Created on Oct 30, 2011

@author: sam
'''

from my2ca.codegen.templating import render_template, Col

def conpool():
    print "Testing template for connection\n"
    print render_template("conpool.py",
                          date= "12,12,12",
                          author= "Test Author",
                          keyspace= "testkeyspace",
                          servers=['localhost/1990'],
                          credentials="None"
                          )

def entity():
    print "Testing template for entity\n"
    print render_template("entity.py")
    cols = {
            Col("column1", "str", ""),
            Col("column2", "int", "")
            }
    print render_template("entitytemplate.py",
                          date= "12,12,12",
                          author= "Test Author",
                          entity_name = "SampleEntity",
                          cols = cols
                          )

def main():
    conpool()
    entity()

if __name__ == '__main__':
    main()
