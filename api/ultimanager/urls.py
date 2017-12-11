from django.conf.urls import include, url

from rest_framework import routers

from ultimanager import views


router = routers.DefaultRouter()
router.register('teams', views.TeamViewSet, base_name='team')


urlpatterns = [
    url(
        r'^games/(?P<pk>[0-9]+)/$',
        views.GameDetailView.as_view(),
        name='game-detail'
    ),

    url(
        r'^games/(?P<pk>[0-9]+)/points/$',
        views.PointListView.as_view(),
        name='point-list'
    ),

    url(
        r'^players/(?P<pk>[0-9]+)/$',
        views.PlayerDetailView.as_view(),
        name='player-detail'
    ),

    url(
        r'^points/(?P<pk>[0-9]+)/$',
        views.PointDetailView.as_view(),
        name='point-detail'
    ),

    url(
        r'^points/(?P<pk>[0-9]+)/possessions/$',
        views.PossessionListView.as_view(),
        name='possession-list'
    ),

    url(
        r'^possessions/(?P<pk>[0-9]+)/$',
        views.PossessionDetailView.as_view(),
        name='possession-detail'
    ),

    url(
        r'^teams/(?P<pk>[0-9]+)/games/$',
        views.GameListView.as_view(),
        name='game-list'
    ),

    url(
        r'^teams/(?P<pk>[0-9]+)/players/$',
        views.PlayerListView.as_view(),
        name='player-list'
    ),

    # Fallback to URLs from the router
    url(r'^', include(router.urls)),
]
