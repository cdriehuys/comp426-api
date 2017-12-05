from django.conf.urls import url

from account import views


urlpatterns = [
    url(
        r'^profile/$',
        views.ProfileView.as_view(),
        name='profile',
    ),

    url(
        r'^register/$',
        views.RegistrationView.as_view(),
        name='register'
    ),
]
