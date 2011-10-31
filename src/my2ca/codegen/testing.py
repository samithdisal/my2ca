'''
Created on Aug 26, 2011

@author: sam
'''
import datetime
import mako.template

if __name__ == '__main__':
    temp = mako.template.Template(filename="../../../templates/conpool.py.template")
    print (temp.render(
                       author="Samith D Sandanayake",
                       date=datetime.date.today().__str__(),
                       keyspace="mego",
                       servers="['localhost/1990']",
                       credentials="None"
                       ))

