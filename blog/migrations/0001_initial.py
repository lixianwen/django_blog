# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-04-21 06:57
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='\u4f5c\u8005')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='e-mail')),
            ],
        ),
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64, verbose_name='\u6807\u9898')),
                ('body', models.TextField(verbose_name='\u6b63\u6587')),
                ('pub_date', models.DateField(verbose_name='\u53d1\u8868\u65e5\u671f')),
                ('enable_comments', models.BooleanField(verbose_name='\u5141\u8bb8\u8bc4\u8bba')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Author')),
            ],
        ),
    ]