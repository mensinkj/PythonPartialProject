# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1427989687.753481
_enable_loop = True
_template_filename = 'c:\\test_dmp\\homepage\\templates/password_reset_email.html'
_template_uri = 'password_reset_email.html'
_source_encoding = 'ascii'
import os, os.path, re
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        __M_writer('{% load i18n %}{% autoescape off %}\n{% blocktrans %}You\'re receiving this email because you requested a password reset for your user account at {{ site_name }}.{% endblocktrans %}\n\n{% trans "Please go to the following page and choose a new password:" %}\n{% block reset_link %}\n{{ protocol }}://{{ domain }}{% url \'password_reset_confirm\' uidb64=uid token=token %}\n{% endblock %}\n{% trans "Your username, in case you\'ve forgotten:" %} {{ user.get_username }}\n\n{% trans "Thanks for using our site!" %}\n\n{% blocktrans %}The {{ site_name }} team{% endblocktrans %}\n\n{% endautoescape %}\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "ascii", "line_map": {"16": 0, "27": 21, "21": 1}, "uri": "password_reset_email.html", "filename": "c:\\test_dmp\\homepage\\templates/password_reset_email.html"}
__M_END_METADATA
"""
