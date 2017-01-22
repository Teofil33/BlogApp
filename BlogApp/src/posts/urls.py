from django.conf.urls import url

from .views import listView, detailView

urlpatterns = [
    url(r'^$', listView, name="list"),
    url(r'^(?P<id>\d+)/$', detailView, name='detail'),
]