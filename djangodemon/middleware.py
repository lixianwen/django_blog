#!/usr/bin/env python
#coding:utf8

import sys
from django.conf import settings
from django.views.debug import technical_500_response
from django.core.exceptions import PermissionDenied

class IPFilterMiddleware(object):
    '''limited access admin page IP Addresslist'''

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.META.get('HTTP_X_FORWARDED_FOR'):
            ip = request.META.get('HTTP_X_FORWARDED_FOR')
        else:
            ip = request.META.get('REMOTE_ADDR')
        if request.path == '/admin/' and ip not in settings.INTERNAL_IPS:
            raise PermissionDenied
        response = self.get_response(request)
        return response

class UserExceptionMiddleware(object):
    '''when debug=False, only superuser or ip in INTERNAL_IPS allow to view debug information'''

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response

    def process_exception(self, request, exception):
        if request.user.is_superuser or request.META.get('REMOTE_ADDR') in settings.INTERNAL_IPS:
            return technical_500_response(request, *sys.exc_info())
