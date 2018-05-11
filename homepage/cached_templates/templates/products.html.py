# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1423175212.412233
_enable_loop = True
_template_filename = 'C:\\Users\\Joshua\\test_dmp\\homepage\\templates/products.html'
_template_uri = 'products.html'
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
        all_products = context.get('all_products', UNDEFINED)
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
        all_products = context.get('all_products', UNDEFINED)
        def content():
            return render_content(context)
        __M_writer = context.writer()
        __M_writer('\r\n\t<div class="text-left">\r\n\t<a href="/homepage/products.create/" class="btn btn-primary">Create New Product</a>\r\n\t</div>\r\n\t<br>\r\n\t<table id="products_table" class = "table table-striped table-bordered">\t\r\n\t\t<tr>\r\n\t\t\t<th>Name</th>\r\n\t\t\t<th>Description</th>\r\n\t\t\t<th>Category</th>\r\n\t\t\t<th>Current Price</th>\r\n\t\t\t<th>Actions</th>\t\t\r\n\t\t</tr>\r\n')
        for product in all_products:
            __M_writer('\t\t\t<tr>\r\n\t\t\t\t<td>')
            __M_writer(str(product.name))
            __M_writer('</td>\r\n\t\t\t\t<td>')
            __M_writer(str(product.description))
            __M_writer('</td>\r\n\t\t\t\t<td>')
            __M_writer(str(product.category))
            __M_writer('</td>\r\n\t\t\t\t<td>')
            __M_writer(str(product.current_price))
            __M_writer('</td>\r\n\t\t\t\t\t<td>\r\n\t\t\t\t\t\t<a href="/homepage/products.edit/')
            __M_writer(str(product.object_id))
            __M_writer('/" class="btn btn-xs btn-danger">Edit</a> \r\n\t\t\t\t\t</td>\t\t\t\r\n\t\t\t</tr>\t\t\r\n\t\t\t</tr>\t\t\t\r\n')
        __M_writer('\t</table>\t\t\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"line_map": {"64": 23, "65": 28, "35": 1, "71": 65, "45": 3, "27": 0, "52": 3, "53": 16, "54": 17, "55": 18, "56": 18, "57": 19, "58": 19, "59": 20, "60": 20, "61": 21, "62": 21, "63": 23}, "uri": "products.html", "source_encoding": "ascii", "filename": "C:\\Users\\Joshua\\test_dmp\\homepage\\templates/products.html"}
__M_END_METADATA
"""
