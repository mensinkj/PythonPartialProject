# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1427909977.154911
_enable_loop = True
_template_filename = 'c:\\test_dmp\\shopping\\templates/Colonial Breeches.html'
_template_uri = 'Colonial Breeches.html'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['content']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    pass
def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, '/homepage/templates/base.htm', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def content():
            return render_content(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content():
            return render_content(context)
        __M_writer = context.writer()
        __M_writer('\r\n\t<div class="breeches" style="text-align: center;">\r\n\t\t<h1>Colonial Breeches</h1>\r\n\t\t<img src="/static/shopping/media/product_images/1.jpg">\r\n\t\t<h3> Nice Red Colonial Breeches</h3>\r\n\r\n\t\t<a href="/shopping/index/" class="btn btn-warning">Add to Cart</a>\r\n\t</div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "ascii", "filename": "c:\\test_dmp\\shopping\\templates/Colonial Breeches.html", "uri": "Colonial Breeches.html", "line_map": {"56": 50, "34": 1, "27": 0, "44": 3, "50": 3}}
__M_END_METADATA
"""
