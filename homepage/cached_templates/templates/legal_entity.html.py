# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1423078273.061084
_enable_loop = True
_template_filename = 'C:\\Users\\Joshua\\test_dmp\\homepage\\templates/legal_entity.html'
_template_uri = 'legal_entity.html'
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
        all_legal_entity = context.get('all_legal_entity', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
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
        all_legal_entity = context.get('all_legal_entity', UNDEFINED)
        def content():
            return render_content(context)
        __M_writer = context.writer()
        __M_writer('\r\n\t<table id="legal_entity_table" class = "table table-striped table-bordered">\t\r\n\t\t<tr>\r\n\t\t\t<th>Given Name</th>\r\n\t\t\t<th>Address1</th>\r\n\t\t\t<th>City</th>\r\n\t\t\t<th>State</th>\r\n\t\t\t<th>ZIP</th>\r\n\t\t\t<th>email</th>\r\n\t\t\t<th>Action</th>\t\t\r\n\t\t</tr>\r\n')
        for legal_entity in all_legal_entity:
            __M_writer('\t\t\t<tr>\r\n\t\t\t\t<td>')
            __M_writer(str(legal_entity.given_name))
            __M_writer('</td>\r\n\t\t\t\t<td>')
            __M_writer(str(legal_entity.address1))
            __M_writer('</td>\r\n\t\t\t\t<td>')
            __M_writer(str(legal_entity.city))
            __M_writer('</td>\r\n\t\t\t\t<td>')
            __M_writer(str(legal_entity.state))
            __M_writer('</td>\r\n\t\t\t\t<td>')
            __M_writer(str(legal_entity.zip_code))
            __M_writer('</td>\r\n\t\t\t\t<td>')
            __M_writer(str(legal_entity.email))
            __M_writer('</td>\r\n\t\t\t\t<td>Edit | Delete</td>\t\t\r\n\t\t\t</tr>\t\t\t\r\n')
        __M_writer('\t</table>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:\\Users\\Joshua\\test_dmp\\homepage\\templates/legal_entity.html", "line_map": {"64": 20, "65": 20, "66": 21, "35": 1, "68": 25, "40": 26, "74": 68, "46": 3, "59": 17, "67": 21, "53": 3, "54": 14, "55": 15, "56": 16, "57": 16, "58": 17, "27": 0, "60": 18, "61": 18, "62": 19, "63": 19}, "source_encoding": "ascii", "uri": "legal_entity.html"}
__M_END_METADATA
"""
