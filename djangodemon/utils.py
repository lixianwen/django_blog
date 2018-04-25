#!/usr/bin/env python
#coding:utf8

def need_login(login_url):
    def preLogin(function):
        def wrapper(request, *args, **kwargs):
            if not request.user.is_authenticated():
                from django.contrib.auth.views import redirect_to_login
                path = request.get_full_path()
                return redirect_to_login(path, login_url)
            return function(request, *args, **kwargs)
        return wrapper
    return preLogin
