from django.conf.urls.defaults import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	url(r'^admin/', include(admin.site.urls)),
    # Authentication
    url(r'^members/login/$', 'django.contrib.auth.views.login', {'template_name': 'members/login.html'}),
    url(r'^members/logout/$', 'members.views.logout'),
    # Image serving
    url(r'^image/(?P<image_id>\w+)/$', 'images.views.load'),
    url(r'^image/(?P<image_id>\w+)/(?P<width>\w+)/(?P<height>\w+)/$', 'images.views.load'),
    # Member Views
    url(r'^dashboard/$', 'members.views.dashboard'),
    url(r'^members/upload_photo/$', 'members.views.upload_photo'),
    # Group Views
    url(r'^group/create/$', 'game.views.create_group'),
    url(r'^group/(?P<group_id>\w+)/$', 'game.views.group'),
    url(r'^group/(?P<group_id>\w+)/join/$', 'game.views.join_group'),
    # Game Views
    url(r'^game/leaderboard/$', 'game.views.leaderboard'),
    url(r'^game/rules/$', 'django.views.generic.simple.direct_to_template', {'template': 'game/rules.html'}),
    url(r'^game/verify/$', 'game.views.verify'),
    url(r'^game/twilio/$', 'game.views.twilio'),
    url(r'^mailgun/$', 'game.views.mailgun'),
)
