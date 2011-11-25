# -*- encoding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 6
_modified_time = 1321967458.053426
_template_filename='../../../templates/entity.py'
_template_uri='entity.py'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='ascii'
_exports = []


def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u"import pycassa\n\n\nclass entity:\n    \n    def __init__(self):\n        '''\n        entity\n        '''\n        break\n    break")
        return ''
    finally:
        context.caller_stack._pop_frame()


