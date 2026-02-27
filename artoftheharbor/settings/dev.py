from .base import *  # noqa: F401,F403

DEBUG = True

SECRET_KEY = "django-insecure-u%(ga_vap@nh!)eb9uy#kjq)9vp+e=psiv4us!8cdx(ap9)v)4"

ALLOWED_HOSTS = ["*"]

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

# Use simple static storage in dev
STORAGES["staticfiles"]["BACKEND"] = "django.contrib.staticfiles.storage.StaticFilesStorage"

try:
    from .local import *  # noqa: F401,F403
except ImportError:
    pass
