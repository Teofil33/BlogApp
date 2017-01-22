from django.conf.urls import url

from .views import listView, detailView, createView, updateView, deleteView

urlpatterns = [
    url(r'^$', listView, name="list"),
    url(r'^(?P<id>\d+)/$', detailView, name='detail'),
    url(r'^(?P<id>\d+)/edit/$', updateView, name='update'),
    url(r'^(?P<id>\d+)/delete/$', deleteView, name='delete'),
    url(r'^create/$', createView, name='create'),
]