"""permission URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from rbac import views
from app01 import views as app01_views
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^login/$', views.login),
    url(r'^index/$', app01_views.index),
    url(r'^userinfo/$', app01_views.userinfo),
    url(r'^order/$', app01_views.order),
    url(r'^userinfo/add/$', app01_views.adduser),
    url(r'^userinfo/edit/(\d+)/$', app01_views.edituser),
    url(r'^userinfo/edit/(\d+)/$', app01_views.edituser),
]
