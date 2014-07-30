from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'eedit.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^eedith/', include('eedith.urls', namespace="sessions")),
    url(r'^admin/', include(admin.site.urls)),

)
