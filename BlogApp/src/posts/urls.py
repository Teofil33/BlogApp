from django.conf.urls import url

from .views import listView

urlpatterns = [
    url(r'^$', listView, name="list"),
]