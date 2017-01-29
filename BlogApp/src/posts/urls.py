from django.conf.urls import url

from .views import listView, detailView, createView, updateView, deleteView

urlpatterns = [
    url(r'^$', listView, name="list"),
    url(r'^create/$', createView, name='create'),
    #url(r'^(?P<slug>[\w-]+)/$', detailView, name='detail'),
    url(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/(?P<slug>[-\w]+)/$', detailView, name="detail"),
    url(r'^(?P<slug>[\w-]+)/edit/$', updateView, name='update'),
    #url(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/(?P<slug>[-\w]+)/edit/$', updateView, name="update"),
    url(r'^(?P<slug>[\w-]+)/delete/$', deleteView, name='delete'),
    #url(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/(?P<slug>[-\w]+)/delete/$', deleteView, name="delete"), 
]