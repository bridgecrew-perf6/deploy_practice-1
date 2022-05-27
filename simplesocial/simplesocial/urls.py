"""simplesocial URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.HomePage.as_view(), name='home'),
    path('admin/', admin.site.urls), 

    # Using namespace in the include() allows you to include the same app more than once, with a different namespace for each instance.
    # (https://docs.djangoproject.com/en/2.2/topics/http/urls/#reversing-namespaced-urls) in the docs, the polls app is included TWICE   with two different namespaces.
    path('accounts/', include('accounts.urls', namespace='accounts')), 

    # here we are using the default urls.py file of 'django.contrib.auth' module
    path('accounts/', include('django.contrib.auth.urls')), 

    path('test/', views.TestPage.as_view(), name='test'), 
    path('thanks/', views.ThanksPage.as_view(), name='thanks'), 
    path('posts/', include('posts.urls', namespace='posts')), 
    path('groups/', include('groups.urls', namespace='groups')),     
]
