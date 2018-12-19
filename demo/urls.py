from django.conf.urls import include, url
from django.contrib.auth import views as auth_views
from demo.views import *


urlpatterns = [
    url(r'^$', auth_views.login),
    url(r'^logout/$', logout_page),
    url(r'^register/$', register),
    url(r'^register/success/$', register_success),
    url(r'^login/$', home)

    # url(r'^accounts/login/$', auth_views.login),  # If user is not login it will redirect to login page
]
