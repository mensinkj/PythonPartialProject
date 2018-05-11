# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1427902219.167054
_enable_loop = True
_template_filename = 'C:\\test_dmp\\homepage\\templates/users.html'
_template_uri = 'users.html'
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
        all_users = context.get('all_users', UNDEFINED)
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
        all_users = context.get('all_users', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n\t<br>\r\n\t<div class="text-left">\r\n\t\t<a href="/homepage/users.create/" class="btn btn-success">Create New User</a>\r\n\t</div>\r\n\t<br>\r\n\t<table id="users_table" class = "table table-striped table-bordered">\t\r\n\t\t<tr>\r\n\t\t\t<th>ID</th>\r\n\t\t\t<th>User Name</th>\r\n\t\t\t<th>First Name</th>\r\n\t\t\t<th>Last Name</th>\r\n\t\t\t<th>Email</th>\r\n\t\t\t<th>Actions</th>\t\t\r\n\t\t</tr>\r\n')
        for user in all_users:
            __M_writer('\t\t\t<tr>\r\n\t\t\t\t<td>')
            __M_writer(str(user.id))
            __M_writer('</td>\r\n\t\t\t\t<td>')
            __M_writer(str(user.username))
            __M_writer('</td>\r\n\t\t\t\t<td>')
            __M_writer(str(user.first_name))
            __M_writer('</td>\r\n\t\t\t\t<td>')
            __M_writer(str(user.last_name))
            __M_writer('</td>\r\n\t\t\t\t<td>')
            __M_writer(str(user.email))
            __M_writer('</td>\r\n\t\t\t\t<td>\r\n\t\t\t\t<a href="/homepage/users.edit/')
            __M_writer(str(user.id))
            __M_writer('/" class="btn btn-xs btn-danger">Edit</a> \r\n\t\t\t\t</td>\t\t\t\r\n\t\t\t</tr>\t\t\t\r\n')
        __M_writer('\t</table>\t\t\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "ascii", "line_map": {"64": 24, "65": 24, "66": 26, "35": 1, "68": 30, "40": 31, "74": 68, "46": 3, "59": 21, "67": 26, "53": 3, "54": 18, "55": 19, "56": 20, "57": 20, "58": 21, "27": 0, "60": 22, "61": 22, "62": 23, "63": 23}, "uri": "users.html", "filename": "C:\\test_dmp\\homepage\\templates/users.html"}
__M_END_METADATA
"""
