# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1425482603.214733
_enable_loop = True
_template_filename = 'C:\\Users\\Joshua\\test_dmp\\Account\\templates/base.htm'
_template_uri = 'base.htm'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['content']


from django_mako_plus.controller import static_files 

def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        self = context.get('self', UNDEFINED)
        request = context.get('request', UNDEFINED)
        user = context.get('user', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\r\n')
        __M_writer('\r\n')
        __M_writer('\r\n')
        static_renderer = static_files.StaticRenderer(self) 
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['static_renderer'] if __M_key in __M_locals_builtin_stored]))
        __M_writer('\r\n\r\n<!DOCTYPE html>\r\n<html>\r\n  <meta charset="UTF-8">\r\n  <div id="background">\r\n  <head>\r\n    \r\n    <title>Account</title>\r\n    \r\n')
        __M_writer('    <script src="http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js"></script>\r\n    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.1/css/bootstrap.min.css">\r\n    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.1/js/bootstrap.min.js"></script>\r\n    <link rel="icon" type="image/png" href="/static/homepage/media/icon.png">\r\n    \r\n\r\n\r\n    \r\n')
        __M_writer('    ')
        __M_writer(str( static_renderer.get_template_css(request, context)  ))
        __M_writer('\r\n  \r\n  </head>\r\n  <body>\r\n    <header>\r\n      <div style="float: left; padding-left: 20px">\r\n        <h4>\r\n')
        if request.user.is_authenticated():
            __M_writer('            <a href="/Account/index">Welcome ')
            __M_writer(str(user.get_username()))
            __M_writer('</a><br><br>\r\n            <a href="/login.logout_view" class="btn btn-primary" style="float: left;" >Logout</a>\r\n')
        else:
            __M_writer('             <a href="/login/" class="btn btn-primary">Login</a>\r\n')
        __M_writer('        </h4>  \r\n      </div> \r\n      Colonial Heritage Foundation \r\n      <div style="float: right; padding-right: 30px">\r\n        <span> \r\n          <h6>\r\n            <form>\r\n              <span class="glyphicon glyphicon-search" aria-hidden="true"></span> <input type="text" name="search">\r\n            </form>\r\n          </h6>\r\n        </span> \r\n    </header>\r\n    <nav class="navbar navbar-inverse navbar-static-top nav-bar">\r\n      <div class="container">\r\n            <a href="/users/">Users</a>\r\n            <a href="/items/">Items</a>\r\n            <a href="/products/">Products</a>\r\n            <a href="/areas/">Areas</a>\r\n            <a href="/phones/">Phone</a>\r\n            <a href="/photographable/">Photographable Thing</a>\r\n      </div>\r\n    </nav>\r\n      <div class="container-fluid">\r\n        <div id="Left" class="col-md-2">\r\n          <h3>\r\n            <a href="/index">Home</a><br><br>\r\n            <a href="/terms">Terms</a><br><br>\r\n            <a href="/about">About Us</a><br><br>\r\n            <a href="/contact">Contact Us</a>\r\n          <h3>\r\n        </div>\r\n        <div id="Center" class="col-md-8">\r\n          ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('\r\n        </div>\r\n        <div id="Right" class="col-md-2">\r\n          <div class="btn-group-vertical" role="group" style="float: right; padding-top: 50px">\r\n            <a href="/users/" class="btn btn-danger">Users</a>\r\n            <a href="/items/" class="btn btn-danger">Items</a>\r\n            <a href="/products/" class="btn btn-danger">Products</a>\r\n            <a href="/areas/" class="btn btn-danger">Areas</a>\r\n            <a href="/phones/" class="btn btn-danger">Phone</a>\r\n            <a href="/photographable/" class="btn btn-danger">Photographable Thing</a>\r\n          </div>\r\n        </div>\r\n      </div>\r\n    <footer>\r\n      <div id="Footer">\r\n        Copyright 2015\r\n        <link rel="icon" type="image/x-icon" href="favicon.ico" />\r\n      </div>\r\n  </footer>\r\n  </body> \r\n</html>')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content():
            return render_content(context)
        __M_writer = context.writer()
        __M_writer('\r\n          ')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"line_map": {"69": 63, "16": 5, "18": 0, "28": 1, "29": 3, "30": 5, "31": 6, "35": 6, "36": 17, "37": 26, "38": 26, "39": 26, "40": 33, "41": 34, "42": 34, "43": 34, "44": 36, "45": 37, "46": 39, "51": 72, "57": 71, "63": 71}, "source_encoding": "ascii", "uri": "base.htm", "filename": "C:\\Users\\Joshua\\test_dmp\\Account\\templates/base.htm"}
__M_END_METADATA
"""
