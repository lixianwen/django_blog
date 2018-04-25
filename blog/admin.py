# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from models import Author, Entry

# Register your models here.

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'email')

class EntryAdmin(admin.ModelAdmin):
    list_display = ('title', 'body', 'pub_date', 'author', 'enable_comments')
    search_fields = ('title', 'body')
    date_hierarchy = 'pub_date'
    raw_id_fields = ('author',)

admin.site.register(Author, AuthorAdmin)
admin.site.register(Entry, EntryAdmin)
