from .views import ListVideo, Detailvideo
from django.conf.urls import url

urlpatterns = [
    url('videos/$', ListVideo.as_view(), name='lista-video'),
    url('videos/(?P<pk>[0-9]+)$', Detailvideo.as_view(), name='detail-video'),
]
