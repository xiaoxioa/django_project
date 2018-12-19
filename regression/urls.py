from django.conf.urls import include, url
from regression import views


urlpatterns = [
    url(r'^$', views.regression_index, name='regression_index'),
]
