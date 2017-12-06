from django.conf.urls import include, url

from rest_framework import routers

from ultimanager import views


router = routers.DefaultRouter()
router.register('teams', views.TeamViewSet, base_name='team')


urlpatterns = [
    url(r'^', include(router.urls)),
]
