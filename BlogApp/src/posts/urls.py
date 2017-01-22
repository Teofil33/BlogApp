from django.conf.urls import url

from .views import listView, detailView, createView

urlpatterns = [
    url(r'^$', listView, name="list"),
    url(r'^(?P<id>\d+)/$', detailView, name='detail'),
    url(r'^create/$', createView, name='create'),
]