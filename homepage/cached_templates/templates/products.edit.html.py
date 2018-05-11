# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1423175411.921645
_enable_loop = True
_template_filename = 'C:\\Users\\Joshua\\test_dmp\\homepage\\templates/products.edit.html'
_template_uri = 'products.edit.html'
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
    return runtime._inherit_from(context, 'base.htm', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        form = context.get('form', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        product = context.get('product', UNDEFINED)
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
        form = context.get('form', UNDEFINED)
        def content():
            return render_content(context)
        product = context.get('product', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n\t<div style="padding-left: 250px; padding-top: 50px;">\r\n\t\t<form method = "POST">\r\n\t\t\t<table>\r\n\t\t\t\t')
        __M_writer(str( form ))
        __M_writer('\t\t\r\n\t\t\t</table>\r\n\t\t\t<br>\r\n\t\t\t<div style="padding-left:45px">\r\n\t\t\t\t<button type="submit" class="btn btn-primary">Submit</button>\r\n\t\t\t\t<a href="/homepage/products.delete/')
        __M_writer(str( product.object_id ))
        __M_writer('/" class="btn btn-danger">Delete Account</a>\r\n\t\t\t</div>\r\n\t\t</form>\r\n\t</div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"uri": "products.edit.html", "filename": "C:\\Users\\Joshua\\test_dmp\\homepage\\templates/products.edit.html", "source_encoding": "ascii", "line_map": {"64": 58, "36": 1, "54": 3, "55": 7, "56": 7, "57": 12, "58": 12, "27": 0, "46": 3}}
__M_END_METADATA
"""
