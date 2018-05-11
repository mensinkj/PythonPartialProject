# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1428117672.469546
_enable_loop = True
_template_filename = 'c:\\test_dmp\\homepage\\templates/batch.html'
_template_uri = 'batch.html'
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
        all_rentals = context.get('all_rentals', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\r\n\r\n\t')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        all_rentals = context.get('all_rentals', UNDEFINED)
        def content():
            return render_content(context)
        __M_writer = context.writer()
        __M_writer('\r\n\t\t<h1>Overdue Rentals\r\n\t\t<a href=\'/rental/index.batchemail/\' class="btn btn-lg btn-warning" style="float:right;">Send Email</a></h1>\r\n\t\t<table id="rentals_table" class = "table table-striped table-bordered" style="margin-top: 20px;">\t\r\n\t\t\t<tr>\r\n\t\t\t\t<th>ID</th>\r\n\t\t\t\t<th>Item</th>\r\n\t\t\t\t<th>Price</th>\r\n\t\t\t\t<th>Quantity</th>\r\n\t\t\t\t<th>Days Late</th>\t\t\r\n\t\t\t</tr>\r\n')
        for rentals in all_rentals:
            __M_writer('\t\t\t\t<tr>\r\n\t\t\t\t\t<td>')
            __M_writer(str(rentals.id))
            __M_writer('</td>\r\n\t\t\t\t\t<td>')
            __M_writer(str(rentals.name))
            __M_writer('</td>\r\n\t\t\t\t\t<td>')
            __M_writer(str(rentals.price_per_day))
            __M_writer('</td>\r\n\t\t\t\t\t<td>')
            __M_writer(str(rentals.quantity))
            __M_writer('</td>\r\n\t\t\t\t\t<td>')
            __M_writer(str(rentals.days_late))
            __M_writer('</td>\r\n\t\t\t\t</tr>\t\t\t\r\n')
        __M_writer('\t\t</table>\r\n\t')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "ascii", "filename": "c:\\test_dmp\\homepage\\templates/batch.html", "uri": "batch.html", "line_map": {"64": 20, "65": 23, "35": 1, "71": 65, "45": 3, "27": 0, "52": 3, "53": 14, "54": 15, "55": 16, "56": 16, "57": 17, "58": 17, "59": 18, "60": 18, "61": 19, "62": 19, "63": 20}}
__M_END_METADATA
"""
