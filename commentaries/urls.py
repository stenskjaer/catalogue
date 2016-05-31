from django.conf.urls import url

from . import views

app_name = 'commentaries'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>[0-9]+)/$', views.Details.as_view(), name='detail'),
    url(r'^inspected/$', views.Inspected.as_view(), name='inspected'),
    url(r'^relevant/$', views.Relevant.as_view(), name='relevant'),
]
