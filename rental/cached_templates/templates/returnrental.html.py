# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1428114441.367652
_enable_loop = True
_template_filename = 'c:\\test_dmp\\rental\\templates/returnrental.html'
_template_uri = 'returnrental.html'
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
        items = context.get('items', UNDEFINED)
        request = context.get('request', UNDEFINED)
        qty = context.get('qty', UNDEFINED)
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
        items = context.get('items', UNDEFINED)
        request = context.get('request', UNDEFINED)
        qty = context.get('qty', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n\t<h1> Rental Return</h1>\r\n\t<table id="rental_table" class="table table-condensed">\t\r\n\t\t<tr>\r\n\t\t\t<th>ID</th>\r\n\t\t\t<th>Name</th>\r\n\t\t\t<th>Price</th>\r\n\t\t\t<th>Quantity</th>\t\t\r\n\t\t</tr>\r\n')
        for item in items:
            __M_writer('\t\t<tr>\r\n\t\t\t<td>')
            __M_writer(str(item.id))
            __M_writer('</td>\r\n\t\t\t<td>')
            __M_writer(str(item.name))
            __M_writer('</td>\r\n\t\t\t<td>')
            __M_writer(str(item.price_per_day))
            __M_writer('</td>\t\t\t\t\r\n\t\t\t<td>')
            __M_writer(str(qty[0]))
            __M_writer('</td>\t\t\t\t\r\n\t\t</tr>\r\n')
        __M_writer('\t</table>\r\n')
        if request.user.is_authenticated():
            __M_writer('\t\t<input type="text" id="Fee"class="form-control" style="width: 200px; float: left; margin-right: 10px;" placeholder="Fee">\r\n\t\t<a href="/rental/index.checkout/" class="btn btn-danger" style="float: left;" >Add Fee</a>\r\n\t    <a href="/rental/rental_cart.returnitem/" class="btn btn-warning" style="float: right;" >Return</a>\r\n\t    <a href="/rental/index/" class="btn btn-success" style="float: right; margin-right: 10px;" >cancel</a>\r\n')
        else:
            pass
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"uri": "returnrental.html", "line_map": {"64": 16, "65": 17, "66": 17, "27": 0, "68": 21, "37": 1, "70": 26, "77": 70, "47": 3, "67": 20, "69": 22, "56": 3, "57": 12, "58": 13, "59": 14, "60": 14, "61": 15, "62": 15, "63": 16}, "source_encoding": "ascii", "filename": "c:\\test_dmp\\rental\\templates/returnrental.html"}
__M_END_METADATA
"""
