from api.settings import *      # noqa


ALLOWED_HOSTS = [
    'api.ultimanager.com',
    'localhost',
]

DEBUG = False


# Use the local settings created by Ansible if they exist

try:
    from api.local_settings import *    # noqa
except ImportError:
    pass
