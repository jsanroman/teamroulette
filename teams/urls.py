from django.conf.urls import patterns, url, include

urlpatterns = patterns(
    '',
    url(r'^team/$', 'teams.views.team', name='team'),
    url(r'^player/$', 'teams.views.player', name='player'),

    url(r'^api/', include('teams.api_urls')),
)
