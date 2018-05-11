# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1427912056.022069
_enable_loop = True
_template_filename = 'c:\\test_dmp\\event\\templates/index.html'
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
        __M_writer = context.writer()
        __M_writer('\r\n    <div class="content">\r\n      <h3>50th Anniversary!</h3>\r\n      <p> Gove Allen just announced Colonial Heritage foundation\'\'s 50th anniversary event. It will be the biggest event that Colonial Heritage have ever held. Colonial Heritage was just announced as the largest and fastest growing non-profit organization ever!! </p> \r\n      <img src="http://i.ytimg.com/vi/XIK7d5mpY2Q/0.jpg" style="margin-left: 200px;">\r\n      <p> The event is being held at the lavell Edwards football stadium:\r\n      <ul>\r\n      \t<li>1700 North Canyon Road<br>\r\n\t\t\tProvo, UT 84604<br>\r\n\t\t\tUnited States<br>\r\n\t\t</li>\r\n\t  </ul>\r\n\r\n\t  Here are some of the cool handcrafted items that you will be able to purchase the event:\r\n\t  <ul>\r\n\t  \t<li>Personalized Mugs</li>\r\n\t  \t<li>Embroidered Guns</li>\r\n\t  \t<li>Chicken Feet</li>\r\n\t  \t<li>real leather belts</li>\r\n\t  \t<li>hand knit socks</li>\r\n\t  \t<li>colonial wigs</li>\r\n\t  </ul>\r\n    </div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "ascii", "filename": "c:\\test_dmp\\event\\templates/index.html", "uri": "index.html", "line_map": {"56": 50, "34": 1, "27": 0, "44": 3, "50": 3}}
__M_END_METADATA
"""
