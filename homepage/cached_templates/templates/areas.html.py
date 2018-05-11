# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1423192176.752597
_enable_loop = True
_template_filename = 'C:\\Users\\Joshua\\test_dmp\\homepage\\templates/areas.html'
_template_uri = 'areas.html'
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
        all_areas = context.get('all_areas', UNDEFINED)
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
        all_areas = context.get('all_areas', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n\t<div class="text-left">\r\n\t\t<a href="/homepage/areas.create/" class="btn btn-primary">Create New Area</a>\r\n\t</div>\r\n\t<br>\r\n\t<table id="areas_table" class = "table table-striped table-bordered">\t\r\n\t\t<tr>\r\n\t\t\t<th>ID</th>\r\n\t\t\t<th>Name</th>\r\n\t\t\t<th>Description</th>\r\n\t\t\t<th>Place Number</th>\r\n\t\t\t<th>Actions</th>\t\t\r\n\t\t</tr>\r\n')
        for area in all_areas:
            __M_writer('\t\t\t<tr>\r\n\t\t\t\t<td>')
            __M_writer(str(area.object_id))
            __M_writer('</td>\r\n\t\t\t\t<td>')
            __M_writer(str(area.name))
            __M_writer('</td>\r\n\t\t\t\t<td>')
            __M_writer(str(area.description))
            __M_writer('</td>\r\n\t\t\t\t<td>')
            __M_writer(str(area.place_number))
            __M_writer('</td>\r\n\t\t\t\t<td>\r\n\t\t\t\t\t<a href="/homepage/areas.edit/')
            __M_writer(str(area.object_id))
            __M_writer('/" class="btn btn-xs btn-danger">Edit</a> \r\n\t\t\t\t</td>\t\t\r\n\t\t\t</tr>\t\t\t\r\n')
        __M_writer('\t</table>\t\t\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:\\Users\\Joshua\\test_dmp\\homepage\\templates/areas.html", "uri": "areas.html", "source_encoding": "ascii", "line_map": {"64": 23, "65": 23, "66": 27, "35": 1, "40": 28, "46": 3, "59": 19, "72": 66, "53": 3, "54": 16, "55": 17, "56": 18, "57": 18, "58": 19, "27": 0, "60": 20, "61": 20, "62": 21, "63": 21}}
__M_END_METADATA
"""
