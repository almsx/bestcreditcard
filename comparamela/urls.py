#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""comparamela URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.conf import settings
from django.conf.urls.static import static

from app.compare.views import Index
from app.compare.views import Form
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    #url(r'^admin/', include(admin.site.urls)),
    url(r'^$', Index.as_view(), name="index"),
    url(r'^form/$', Form.as_view(), name="formulary"),
]

urlpatterns += staticfiles_urlpatterns()
