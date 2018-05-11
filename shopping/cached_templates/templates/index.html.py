# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1427906403.336149
_enable_loop = True
_template_filename = 'c:\\test_dmp\\shopping\\templates/index.html'
_template_uri = 'index.html'
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
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        catalog_items = context.get('catalog_items', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        def content():
            return render_content(context)
        catalog_items = context.get('catalog_items', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n\t<div style="text-align: center;">\r\n')
        for products in catalog_items:	
            __M_writer('\t\t\t<div class ="item_container">\r\n\t\t\t\t<a href="/shopping/')
            __M_writer(str( products.name ))
            __M_writer('/">\r\n\t\t\t\t<img class="product_picture" src="')
            __M_writer(str( STATIC_URL ))
            __M_writer('shopping/media/product_images/')
            __M_writer(str( products.id ))
            __M_writer('.jpg" />\r\n\t\t\t\t<div class="product_name">')
            __M_writer(str( products.name ))
            __M_writer('</div></a>\r\n\t\t\t\t<div class="product_description">')
            __M_writer(str( products.description ))
            __M_writer('</div><br>\r\n\t\t\t\t<div class="product_price">$')
            __M_writer(str( products.price ))
            __M_writer('</div>\r\n\t\t\t\t\r\n\t\t\t\t<div class="text-bottom" style="bottom: 0px;">\r\n\t\t\t\tQuantity:\r\n\t\t\t\t<input class="control-form qty" id="qty" type="number" method="POST"><br>\r\n\t\t\t\t\t<br><button data-pid="')
            __M_writer(str( products.id ))
            __M_writer('" class="add_button btn btn-warning"> Add to Cart</button>\r\n\t\t\t\t</div>\r\n\t\t\t</div>\r\n')
        __M_writer('\t</div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"line_map": {"64": 9, "65": 9, "66": 10, "67": 10, "68": 11, "69": 11, "70": 16, "71": 16, "72": 20, "78": 72, "27": 0, "36": 1, "41": 21, "47": 3, "55": 3, "56": 5, "57": 6, "58": 7, "59": 7, "60": 8, "61": 8, "62": 8, "63": 8}, "filename": "c:\\test_dmp\\shopping\\templates/index.html", "source_encoding": "ascii", "uri": "index.html"}
__M_END_METADATA
"""
