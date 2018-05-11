# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1428109919.744957
_enable_loop = True
_template_filename = 'c:\\test_dmp/homepage/templates/base.htm'
_template_uri = '/homepage/templates/base.htm'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['content']


from django_mako_plus.controller import static_files 

def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        self = context.get('self', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        user = context.get('user', UNDEFINED)
        request = context.get('request', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n')
        __M_writer('\r\n')
        __M_writer('\r\n')
        static_renderer = static_files.StaticRenderer(self) 
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['static_renderer'] if __M_key in __M_locals_builtin_stored]))
        __M_writer('\r\n\r\n<!DOCTYPE html>\r\n<html>\r\n  <meta charset="UTF-8">\r\n  <meta name="author" content="Joshua Mensink">\r\n  <meta name="description" content="News on colonial events and products">\r\n  <meta name="keywords" content="colonial, Awesome, Heritage, American, BYU, Gove">\r\n  <head>\r\n  <div id="background">\r\n    \r\n    <title>Colonial Heritage Foundation</title>\r\n    \r\n')
        __M_writer('    <script src="http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js"></script>\r\n    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.1/css/bootstrap.min.css">\r\n    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.1/js/bootstrap.min.js"></script>\r\n    <link rel="icon" type="image/png" href="/static/homepage/media/icon.png">\r\n    <script src="')
        __M_writer(str( STATIC_URL ))
        __M_writer('homepage/media/jqueryforms.js"></script>\r\n    <script src="')
        __M_writer(str(STATIC_URL ))
        __M_writer('homepage/media/jquery.loadmodal.js"></script>\r\n\r\n    \r\n')
        __M_writer('    ')
        __M_writer(str( static_renderer.get_template_css(request, context)  ))
        __M_writer('\r\n  \r\n  </head>\r\n  <body>\r\n    <div class="Background">\r\n      <header>\r\n        <div class="navigationbar">\r\n')
        if request.user.is_authenticated():
            __M_writer('            <nav class="navbar navbar-inverse" style="padding-right: 80px;">\r\n              <ul class="nav navbar-nav">\r\n                <li><a href="/login.logout_view">Logout</a></li>\r\n                <li class="dropdown">\r\n                  <a href=""class="dropdown-toggle" data-toggle="dropdown" role="button">Edit Content<span class="caret"></span></a>\r\n                  <ul class="dropdown-menu" style="background-color: rgba(0,0,0,0.5);" role="menu">\r\n                    <li><a href="/homepage/users" style="color: white;">Users</a></li>\r\n                    <li class="divider" style="color: black;"></li>\r\n                    <li><a href="/homepage/items" style="color: white;">items</a></li>\r\n                    <li><a href="/homepage/products" style="color: white;">products</a></li>\r\n                  </ul>\r\n                </li>\r\n                <li class=\'dropdown\'>\r\n                  <a href=""class="dropdown-toggle" data-toggle="dropdown" role="button">Rentals<span class="caret"></span></a>\r\n                  <ul class="dropdown-menu" style="background-color: rgba(0,0,0,0.5);" role="menu">\r\n                    <li><a href="/rental/index.returnrental" style="color: white;">Returns</a></li>\r\n                    <li class="divider" style="color: black;"></li>\r\n                    <li><a href="/homepage/index.batch" style="color: white;">Overdue Rentals</a></li>\r\n                  </ul>\r\n                </li>\r\n                <li><input type="text" id="search"class="form-control" style="width: 500px; margin-top: 10px" placeholder="Search"><li>\r\n                <li style="float: right"><a href="/shopping/index.checkout/" class="btn btn-warning btn-lg navbar-right" style="color: white; margin-top: 2px; margin-bottom:2px;" >Checkout</a></li>\r\n              </ul>\r\n            </nav>\r\n')
        else:
            __M_writer('            <nav class="navbar navbar-inverse">\r\n              <ul class="nav navbar-nav">\r\n                <li>\r\n                  <button type-"button" id="show_login_dialog" class="btn btn-warning btn-lg" style="margin-top: 10px;">Login\r\n                  </button></li>\r\n                <li><a href="/Account/index.create">Create a new Account</a></li>\r\n                <input type="text" id="search" class="form-control navbar-right" style="margin-right: 20px; margin-top: 20px; width: 500px;" placeholder="Search">\r\n              </ul>\r\n            </nav>\r\n')
        __M_writer('        </div>\r\n        <div style="float: left; padding-left: 20px">\r\n')
        if request.user.is_authenticated():
            __M_writer('              <h4><a href="/Account/index.edituser/')
            __M_writer(str( user.id ))
            __M_writer('/">Welcome ')
            __M_writer(str(user.get_username()))
            __M_writer('</a></h4>\r\n')
        else:
            pass
        __M_writer('        </div> \r\n        <div>\r\n          <h1><span style="font-family:Times; font-size:48pt;">Colonial Heritage Foundation</span></h1>\r\n        </div>\r\n      </header>\r\n      <div class="container-fluid">\r\n        <div id="Left" class="col-md-2" style="padding-top: 0px">\r\n          <h3 style="padding-top:25px;">\r\n            <a href="/homepage/index">Home</a><br><br>\r\n            <a href="/event/index">Events</a><br><br>\r\n            <a href="/shopping/index">Shop</a><br><br>\r\n            <a href="/rental/index">Rent</a><br><br>\r\n            <a href="/homepage/terms">Terms</a><br><br>\r\n            <a href="/homepage/about">About Us</a><br><br>\r\n            <a href="/homepage/contact">Contact Us</a>\r\n          <h3>\r\n        </div>\r\n        <div id="Center" class="col-md-8">\r\n          ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('\r\n        </div>\r\n      </div>\r\n    </body>\r\n    <footer>\r\n      <div id="Footer">\r\n        Copyright 2015\r\n        <link rel="icon" type="image/x-icon" href="favicon.ico" />\r\n      </div>\r\n      <script>\r\n        (function(i,s,o,g,r,a,m){i[\'GoogleAnalyticsObject\']=r;i[r]=i[r]||function(){\r\n        (i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),\r\n        m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)\r\n        })(window,document,\'script\',\'//www.google-analytics.com/analytics.js\',\'ga\');\r\n\r\n        ga(\'create\', \'UA-61450130-1\', \'auto\');\r\n        ga(\'send\', \'pageview\');\r\n\r\n      </script>\r\n    </footer> \r\n  </div>\r\n</html>\r\n\r\n\r\n')
        __M_writer('    ')
        __M_writer(str( static_renderer.get_template_js(request, context)  ))
        __M_writer('\r\n')
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
{"uri": "/homepage/templates/base.htm", "source_encoding": "ascii", "filename": "c:\\test_dmp/homepage/templates/base.htm", "line_map": {"64": 122, "65": 122, "66": 122, "72": 96, "78": 96, "16": 5, "18": 0, "84": 78, "29": 1, "30": 3, "31": 5, "32": 6, "36": 6, "37": 20, "38": 24, "39": 24, "40": 25, "41": 25, "42": 29, "43": 29, "44": 29, "45": 36, "46": 37, "47": 61, "48": 62, "49": 72, "50": 74, "51": 75, "52": 75, "53": 75, "54": 75, "55": 75, "56": 76, "58": 78, "63": 97}}
__M_END_METADATA
"""
