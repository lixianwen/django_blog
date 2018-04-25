# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=50, verbose_name=u'作者')
    email = models.EmailField(blank=True, verbose_name='e-mail')

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = u'作者'
        verbose_name_plural = verbose_name

class Entry(models.Model):
    title = models.CharField(max_length=64, verbose_name=u'标题')
    body = models.TextField(verbose_name=u'正文')
    pub_date = models.DateField(verbose_name=u'发表日期')
    author = models.ForeignKey(Author)
    enable_comments = models.BooleanField(verbose_name=u'允许评论')

    class Meta:
        verbose_name = u'文章'
        verbose_name_plural = verbose_name
        ordering = ['-pub_date']
