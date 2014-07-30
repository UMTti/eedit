from django.conf.urls import patterns, url

from eedith import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'), 
    # ex: /sessions/5/
    url(r'^(?P<session_id>\d+)/$', views.detail, name='detail'),
)