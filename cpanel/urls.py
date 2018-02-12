"""pimek URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.conf.urls import url
from cpanel import views
from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('',  views.dashboard, name='dashboard'),
    path('/dashboard',  views.dashboard, name='dashboard'),
    path('/signin',  views.signin, name='signin'),
    path('/notifications',  views.notifications, name='notifications'),
    path('/tables',  views.tables, name='tables'),
    path('/set_mail',  views.set_mail, name='mail'),
    path('/set_pass',  views.set_pass, name='pass'),
    path('/settings',  views.settings, name='settings'),
    path('/add_product',  views.add_product, name='add_product'),
    path('/product/<int:id>/',  views.product, name='product'),
    path('/edit_product/<int:id>/',  views.edit_product, name='edit_product'),
    path('/delete_product/<int:id>/',  views.delete_product, name='delete_product'),
    path('/logout',  auth_views.logout),
]