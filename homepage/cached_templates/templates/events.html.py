# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1423076011.372723
_enable_loop = True
_template_filename = 'C:\\Users\\Joshua\\test_dmp\\homepage\\templates/events.html'
_template_uri = 'events.html'
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
        all_events = context.get('all_events', UNDEFINED)
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
        all_events = context.get('all_events', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n\t\'\'\'<table id="events_table" class = "table table-striped table-bordered">\t\r\n\t\t<tr>\r\n\t\t\t<th>Start Date</th>\r\n\t\t\t<th>End Date</th>\r\n\t\t\t<th>Map File</th>\r\n\t\t\t<th>Action</th>\t\t\r\n\t\t</tr>\r\n')
        for event in all_events:
            __M_writer('\t\t\t<tr>\r\n\t\t\t\t<td>')
            __M_writer(str(event.start_date))
            __M_writer('</td>\r\n\t\t\t\t<td>')
            __M_writer(str(event.end_date))
            __M_writer('</td>\r\n\t\t\t\t<td>')
            __M_writer(str(event.map_file))
            __M_writer('</td>\r\n\t\t\t\t<td>Edit | Delete</td>\t\t\r\n\t\t\t</tr>\t\t\t\r\n')
        __M_writer("\t</table>\t'''\r\n\ttesting\t\r\n")
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"uri": "events.html", "line_map": {"35": 1, "68": 62, "40": 21, "46": 3, "59": 14, "53": 3, "54": 11, "55": 12, "56": 13, "57": 13, "58": 14, "27": 0, "60": 15, "61": 15, "62": 19}, "source_encoding": "ascii", "filename": "C:\\Users\\Joshua\\test_dmp\\homepage\\templates/events.html"}
__M_END_METADATA
"""
