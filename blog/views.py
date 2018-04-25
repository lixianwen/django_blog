# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import datetime
from django.shortcuts import render
from models import Author, Entry
from django.contrib.auth.decorators import permission_required
from django.contrib import messages
from django.urls import reverse
from django.http import HttpResponseRedirect

# Create your views here.

def index(request):
    pass

@permission_required('blog.add_entry')
def addEntry(request):
    if request.method == 'POST':
        title = request.POST.get('title', '')
        context = request.POST.get('context', '')
        author_name = request.POST.get('author')
        can_comment = request.POST.get('can_comment', False)
        entry = Entry(title=title, body=context, author=Author.objects.get(name=author_name), pub_date=datetime.date.today(), enable_comments=can_comment)
        entry.save()
        messages.add_message(request, messages.SUCCESS, u'文章发表成功')
        return HttpResponseRedirect(reverse('index'))
    author_list = Author.objects.all()
    return render(request, 'blog/addentry.html', locals())

def showEntry(request):
    pk = request.GET.get('p')
    entry = Entry.objects.get(id=int(pk))
    return render(request, 'blog/showentry.html', locals())
