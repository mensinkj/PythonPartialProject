# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1427913995.706797
_enable_loop = True
_template_filename = 'c:\\test_dmp\\shopping\\templates/shopping_cart.html'
_template_uri = 'shopping_cart.html'
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
    return runtime._inherit_from(context, '/homepage/templates/base_ajax.htm', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        items = context.get('items', UNDEFINED)
        request = context.get('request', UNDEFINED)
        user = context.get('user', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        qty = context.get('qty', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('\t\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        items = context.get('items', UNDEFINED)
        request = context.get('request', UNDEFINED)
        user = context.get('user', UNDEFINED)
        def content():
            return render_content(context)
        qty = context.get('qty', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n\t<table id="shopping_table" class="table table-condensed">\t\r\n\t\t<tr>\r\n\t\t\t<th>ID</th>\r\n\t\t\t<th>Name</th>\r\n\t\t\t<th>Quantity</th>\r\n\t\t\t<th>Action</th>\t\t\r\n\t\t</tr>\r\n')
        for item in items:
            __M_writer('\t\t<tr>\r\n\t\t\t<td>')
            __M_writer(str(item.id))
            __M_writer('</td>\r\n\t\t\t<td>')
            __M_writer(str(item.name))
            __M_writer('</td>\t\t\t\t\r\n\t\t\t<td>')
            __M_writer(str(qty[0]))
            __M_writer('</td>\t\t\t\t\r\n\t\t\t<td>\r\n\t\t\t\t<a href="/shopping/shopping_cart.delete/')
            __M_writer(str(user.id))
            __M_writer('/" class="btn btn-xs btn-danger">Delete</a> \r\n\t\t\t</td>\r\n\t\t</tr>\r\n')
        __M_writer('\t</table>\r\n')
        if request.user.is_authenticated():
            __M_writer('          <a href="/shopping/index.checkout/" class="btn btn-warning" style="float: right;" >Checkout</a>\r\n')
        else:
            pass
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"line_map": {"64": 14, "65": 14, "66": 15, "27": 0, "68": 17, "69": 17, "38": 1, "71": 22, "72": 23, "73": 24, "43": 26, "70": 21, "80": 73, "49": 3, "67": 15, "59": 3, "60": 11, "61": 12, "62": 13, "63": 13}, "uri": "shopping_cart.html", "source_encoding": "ascii", "filename": "c:\\test_dmp\\shopping\\templates/shopping_cart.html"}
__M_END_METADATA
"""
