import environ

from . import *

env = environ.Env()
environ.Env.read_env()

SECRET_KEY = env("SECRET_KEY")
DEBUG = False
ALLOWED_HOSTS = ["127.0.0.1"]
CORS_ALLOWED_ORIGINS = ["http://localhost:8000", "http://127.0.0.1:8000"]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "HOST": env("DATABASE_HOST"),
        "PORT": env("DATABASE_PORT"),
        "USER": env("DATABASE_USER"),
        "PASSWORD": env("DATABASE_PASSWORD"),
        "NAME": env("DATABASE_NAME"),
    },
}

REST_FRAMEWORK = {
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly"
    ],
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    ],
    "EXCEPTION_HANDLER": "arol.exception_handler.exception_handler",
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.PageNumberPagination",
    "PAGE_SIZE": 50,
}
