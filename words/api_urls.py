from django.conf.urls import url, include
from words import api

urlpatterns = [
    url('^check', api.check),
    url('^start_session', api.register),
]