#from django.conf.urls import patterns, url

from django.conf.urls import url
#from django.contrib.auth.views import login
from django.contrib.auth.views import LoginView

from demo import views as demo_views

from django.contrib import admin
admin.autodiscover()

urlpatterns = [
    #'',
    url(r'^$', demo_views.index, name='index'),
    url(r'^saml/acs',demo_views.acs, name='acs'),
]
