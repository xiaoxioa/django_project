from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView
from upload import views
from feature_select import views as fViews


urlpatterns = [
    url(r'^success/$', views.upload_success),
    url(r'^$', views.upload_file),
    url(r'^feature_select/$', fViews.feature_select_index, name='feature_select')
]
