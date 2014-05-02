# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from django.conf import settings
from django.conf.urls.static import static

from myapp.views import FileManagerView, FileRemoveView

urlpatterns = patterns('',
                       url(r'^$', FileManagerView.as_view(), name='main'),
                       url(r'^delete/(?P<pk>\d+)/$', FileRemoveView.as_view(), name='delete'),
                       )+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
