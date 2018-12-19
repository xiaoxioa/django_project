from django.conf.urls import include, url
from result import views


urlpatterns = [
    url(r'^$', views.result_index, name='result_index'),
]
