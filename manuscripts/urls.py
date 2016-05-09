from django.conf.urls import url

from . import views

app_name = 'manuscripts'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url('^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail')
]
