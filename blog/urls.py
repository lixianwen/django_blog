from django.conf.urls import url
from views import *

urlpatterns = [
    url(r'^$', index),
    url(r'^add/$', addEntry, name='addentry'),
    url(r'^show/$', showEntry, name='showentry'),
]
