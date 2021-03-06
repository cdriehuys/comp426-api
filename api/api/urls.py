"""api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin

from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.documentation import include_docs_urls


urlpatterns = [
    url(
        r'^account/',
        include('account.urls')
    ),

    url(
        r'^admin/',
        admin.site.urls
    ),

    # Allows authentication when using the browseable API.
    url(
        r'^api-auth/',
        include('rest_framework.urls', namespace='rest_framework')
    ),

    url(
        r'^auth/login/$',
        obtain_auth_token
    ),

    url(
        r'^docs/',
        include_docs_urls('UltiManager API')
    ),

    url(
        r'^team-management/',
        include('ultimanager.urls', namespace='ultimanager')
    ),
]


# If we are in development, have Django serve media files. Normally
# these files are served by the webserver (NGINX).
if settings.DEBUG:
    from django.conf.urls.static import static

    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT)
