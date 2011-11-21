'''
Created on Nov 21, 2011

@author: sam
'''

import pydoc
import os
from my2ca.codegen.templating import render_template

_input_folder = "generated_code"
_output_folder = "generated_doc"
_readme_file = os.path.join([_output_folder,"README"])

def generate_doc():
    """
    Generates python api documentation for the generated code
    """
    if not os.path.exists(_input_folder):
        return False
    
    if not os.path.exists(_output_folder):
        os.makedirs(_output_folder)
        pass
    else:
        os.rmdir(_output_folder)
        os.makedirs(_output_folder)
        pass
    
    pydoc.writedocs(_output_folder, _input_folder)
    readme = render_template("README_DOC")
    readme_file = file(_readme_file)
    readme_file.write(readme)
    return True

if __name__ == '__main__':
    if generate_doc():
        print "DONE"
        pass
    else:
        print "Error"
        pass
    pass
