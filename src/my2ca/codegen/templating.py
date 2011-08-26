'''
Created on Aug 14, 2011

@author: sam
'''

import mako


'''
Template Lookup Directories and Include paths.
'''
template_lookup_dir = mako.lookup.TemplateLookup(directories=['/templates'],
                                                 module_directory='/generated_output',
                                                 output_encoding='utf-8')



def render_template(template, **args):
    '''
    Render the template file given by the <i>template</i> argument,
    using <i>args</i> as the data.
    '''
    t = template_lookup_dir.get_template(template)
    return t.render_unicode(**args)




def gen_module(modulename, outpath, data):
    '''
    Generate the module using master template given in <i>modulename</i>,
    using data in <i>data</i>,
    outputs to <i>outpath</i>
    '''
    ofile = open(outpath, 'w')
    if ofile == None:
        raise IOError("given path is not writable")
    if ofile.closed:
        raise IOError("file created but closed to access")
    ofile.write(render_template(modulename, data))
    ofile.flush()
    ofile.close()

