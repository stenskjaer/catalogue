from django.conf.urls import url, include
from rest_framework import routers

from api import views


# Routers for the API
router = routers.DefaultRouter()
router.register(r'^manuscripts', views.ManuscriptViewSet)
router.register(r'^texts', views.TextViewSet)


app_name = 'api'
urlpatterns = [
    url(r'^', include(router.urls)),
    # url('^manuscripts/(?P<pk>[0-9]+)/$', views.ManuscriptDetailView.as_view(), name='manuscript-detail')
    # url('^manuscript/(?P<manuscript_id>[0-9]+)/$', views.manuscript_json, name='manuscript-detail')
]
