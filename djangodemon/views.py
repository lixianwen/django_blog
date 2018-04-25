#!/usr/bin/env python
#coding:utf8

from django.shortcuts import render
from blog.models import Entry
from django.contrib import auth
from django.contrib import messages
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.http import HttpResponse
from verifycode import VeifyCode
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def index(request):
    entry_list = Entry.objects.all()
    paginator = Paginator(entry_list, 3, 2)
    page = request.GET.get('page')
    try:
        entrys = paginator.page(page)
    except PageNotAnInteger:
        entrys = paginator.page(1)
    except EmptyPage:
        entrys = paginator.page(paginator.num_pages)
    return render(request, 'index.html', locals())

def loginview(request):
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)
        if not user:
            error = 'Invalid user or incorrect password.'
            messages.add_message(request, messages.ERROR, error)
            return HttpResponseRedirect(reverse('loginview'))
        elif not user.is_staff:
            error = 'user {0} is not allow logged in.'.format(username)
            messages.add_message(request, messages.ERROR, error)
            return HttpResponseRedirect(reverse('loginview'))
        else:
            auth.login(request, user)
            return HttpResponseRedirect(reverse('index'))
    return render(request, 'registration/login.html')

def logoutview(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('index'))

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        pwdrepeat = request.POST.get('pwdrepeat')
        email = request.POST.get('email', None)
        verifycode = request.POST.get('verifycode').lower()
        _text = request.session.get('code_text').lower()
        print(verifycode)
        print(_text)
        user = auth.authenticate(username=username, password=password)
        try:
            user_exist = User.objects.get(username=username)
        except Exception:
            user_exist = None
        if password != pwdrepeat:
            error = u'两次输入的密码不一致'
            messages.add_message(request, messages.ERROR, error)
            return HttpResponseRedirect(reverse('register'))
        elif user or user_exist:
            error = u'该用户名已被注册'
            messages.add_message(request, messages.ERROR, error)
            return HttpResponseRedirect(reverse('register'))
        elif verifycode != _text:
            messages.add_message(request, messages.ERROR, u'验证码错误，请重新输入')
            request.session.pop('code_text')
            return HttpResponseRedirect(reverse('register'))
        else:
            new_user = User.objects.create_user(username=username, email=email, password=password)
            new_user.save()
            messages.add_message(request, messages.SUCCESS, u'欢迎，用户：{0} 已注册成功'.format(username))
            messages.add_message(request, messages.SUCCESS, u'请联系管理员开通相关权限'.format(username))
            return HttpResponseRedirect('/thankyou/')
#    print(request.session.get('code_text'), '######')
    return render(request, 'register.html')

def image(request):
    verifyCode = VeifyCode()
    content, buf_str = verifyCode.getImage()
    request.session['code_text'] = content
#    print(request.session['code_text'])
    return HttpResponse(buf_str, content_type='image/png')
