from api.settings import *      # noqa


ALLOWED_HOSTS = [
    'api.ultimanager.com',
    'localhost',
]

DEBUG = False


# Security Settings for HTTPS

CSRF_COOKIE_SECURE = True
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True


# Use the local settings created by Ansible if they exist

try:
    from api.local_settings import *    # noqa
except ImportError:
    pass
