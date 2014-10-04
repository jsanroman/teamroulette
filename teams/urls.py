from django.conf.urls import patterns, url

urlpatterns = patterns(
    '',
    url('^team/$', 'teams.views.team', name='team'),
    url('^player/$', 'teams.views.player', name='player'),
)
