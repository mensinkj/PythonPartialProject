# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1428118987.811947
_enable_loop = True
_template_filename = 'c:\\test_dmp\\rental\\templates/batchemail.html'
_template_uri = 'batchemail.html'
_source_encoding = 'ascii'
import os, os.path, re
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        all_rentals = context.get('all_rentals', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('<html>\r\n\t<head>\r\n\t</head>\r\n\t<body>\r\n\t\t<h1>Overdue Rentals</h1>\r\n\t\t<a href=\'/rentals/index.batchemail/\' class="btn btn-lg btn-warning" style="float:right;">Send Email</a></h1>\r\n\t\t<table id="rentals_table" class = "table table-striped table-bordered" style="margin-top: 20px;">\t\r\n\t\t\t<tr>\r\n\t\t\t\t<th>ID</th>\r\n\t\t\t\t<th>Item</th>\r\n\t\t\t\t<th>Price</th>\r\n\t\t\t\t<th>Quantity</th>\r\n\t\t\t\t<th>Days Late</th>\t\t\r\n\t\t\t</tr>\r\n')
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
        __M_writer('\t\t</table>\r\n\t</body>\r\n</html>')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "c:\\test_dmp\\rental\\templates/batchemail.html", "uri": "batchemail.html", "line_map": {"32": 20, "33": 21, "34": 21, "35": 24, "41": 35, "16": 0, "22": 1, "23": 15, "24": 16, "25": 17, "26": 17, "27": 18, "28": 18, "29": 19, "30": 19, "31": 20}, "source_encoding": "ascii"}
__M_END_METADATA
"""
