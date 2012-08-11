from django.conf.urls import patterns, include, url
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'pytube.views.home', name='home'),
    url(r'^view/(?P<video_id>\d+)$', 'pytube.views.view', name='view'),
    url(r'^login$', 'pytube.views.login_user',
        {'template_name': 'login.html'}, name='login'),
    url(r'^logout$', 'django.contrib.auth.views.logout',
        {'next_page': '/'}, name='logout'),
    url(r'^register$', 'pytube.views.register_user', name='register'),
    url(r'^upload$', 'pytube.views.upload', name='upload'),

    url(r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
                'document_root': settings.MEDIA_ROOT,
            }),
    )
