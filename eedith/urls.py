from django.conf.urls import patterns, url

from eedith import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'), 
    # ex: /sessions/5/
    url(r'^(?P<session_id>\d+)/$', views.detail, name='detail'),
    url(r'^(?P<session_id>\d+)/update_description/$', views.update_description, name='update_description'),
    url(r'create_session/', views.create_session, name="create_session"),
    url(r'^(?P<session_id>\d+)/end_session/$', views.end_session, name='end_session'),
)