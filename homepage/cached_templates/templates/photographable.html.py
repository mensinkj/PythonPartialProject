# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1423192349.446474
_enable_loop = True
_template_filename = 'C:\\Users\\Joshua\\test_dmp\\homepage\\templates/photographable.html'
_template_uri = 'photographable.html'
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
        def content():
            return render_content(context._locals(__M_locals))
        all_pt = context.get('all_pt', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('\t')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content():
            return render_content(context)
        all_pt = context.get('all_pt', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n\t<div class="text-left">\r\n\t\t<a href="/homepage/photographable.create/" class="btn btn-primary">Create New Photographable Thing</a>\r\n\t</div>\r\n\t<br>\r\n\t<table id="pt_table" class = "table table-striped table-bordered">\t\r\n\t\t<tr>\r\n\t\t\t<th>ID</th>\t\r\n\t\t\t<th>Action</th>\t\r\n\t\t</tr>\r\n')
        for photographablething in all_pt:
            __M_writer('\t\t\t<tr>\r\n\t\t\t\t<td>')
            __M_writer(str(photographablething.object_id))
            __M_writer('</td>\r\n\t\t\t\t<td>\r\n\t\t\t\t\t<a href="/homepage/photographable.edit/')
            __M_writer(str(photographablething.object_id))
            __M_writer('/" class="btn btn-xs btn-danger">Edit</a> \r\n\t\t\t\t</td>\t\t\r\n\t\t\t</tr>\t\t\t\r\n')
        __M_writer('\t</table>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"line_map": {"66": 60, "35": 1, "40": 22, "46": 3, "59": 17, "53": 3, "54": 13, "55": 14, "56": 15, "57": 15, "58": 17, "27": 0, "60": 21}, "uri": "photographable.html", "filename": "C:\\Users\\Joshua\\test_dmp\\homepage\\templates/photographable.html", "source_encoding": "ascii"}
__M_END_METADATA
"""
