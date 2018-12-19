from django.conf.urls import include, url
from django.contrib import admin
from feature_select import views


urlpatterns = [
    url(r'^$', views.feature_select_index, name = 'feature_select_index'),
    url(r'^success/$', views.feature_success),
]
