"""
URL configuration for djangocourse project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.views.generic.base import RedirectView
from allauth.account.views import SignupView
# 1. Development
from  django.conf import settings

urlpatterns = [
    path('articles/', include('app.urls')),
    path('admin/', admin.site.urls),
    # logowanie
    path('accounts/', include('allauth.urls')),
    # aby przekierowac na strone glowna po wejsciu na domyslny url (localhost:8000)
    path('', SignupView.as_view(), name='account_signup'),
    path('accounts/signup/', RedirectView.as_view(url='/')),
]
# 2. Deployment
if settings.DEBUG:
    urlpatterns += [
        path('__debug__/', include('debug_toolbar.urls')),
        path('__reload__/', include('django_browser_reload.urls')),
    ]   