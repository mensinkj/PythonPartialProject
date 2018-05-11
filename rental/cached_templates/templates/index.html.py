# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1428104584.007799
_enable_loop = True
_template_filename = 'c:\\test_dmp\\rental\\templates/index.html'
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
        def content():
            return render_content(context._locals(__M_locals))
        rental_items = context.get('rental_items', UNDEFINED)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
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
        rental_items = context.get('rental_items', UNDEFINED)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n\t<div style="text-align: center;">\r\n')
        for rentals in rental_items:	
            __M_writer('\t\t\t<div class ="item_container">\r\n\t\t\t\t<a href="/rental/')
            __M_writer(str( rentals.name ))
            __M_writer('/">\r\n\t\t\t\t<img class="rental_picture" src="')
            __M_writer(str( STATIC_URL ))
            __M_writer('rental/media/product_images/')
            __M_writer(str( rentals.id ))
            __M_writer('.jpg" />\r\n\t\t\t\t<div class="rental_name">')
            __M_writer(str( rentals.name ))
            __M_writer('</div></a>\r\n\t\t\t\t<div class="rental_description">')
            __M_writer(str( rentals.description ))
            __M_writer('</div><br>\r\n\t\t\t\t<div class="rental_price">$')
            __M_writer(str( rentals.price_per_day ))
            __M_writer('</div>\r\n\t\t\t\t\r\n\t\t\t\t<div class="text-bottom" style="bottom: 0px;">\r\n\t\t\t\tQuantity:\r\n\t\t\t\t<input class="control-form qty" id="qty" type="number" method="POST"><br>\r\n\t\t\t\t\t<br><button data-pid="')
            __M_writer(str( rentals.id ))
            __M_writer('" class="add_button btn btn-warning"> Add to Cart</button>\r\n\t\t\t\t</div>\r\n\t\t\t</div>\r\n')
        __M_writer('\t</div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"uri": "index.html", "line_map": {"64": 9, "65": 10, "66": 10, "67": 11, "68": 11, "69": 16, "70": 16, "71": 20, "77": 71, "27": 0, "36": 1, "46": 3, "54": 3, "55": 5, "56": 6, "57": 7, "58": 7, "59": 8, "60": 8, "61": 8, "62": 8, "63": 9}, "source_encoding": "ascii", "filename": "c:\\test_dmp\\rental\\templates/index.html"}
__M_END_METADATA
"""
