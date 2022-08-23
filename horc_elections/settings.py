import environ
import dj_database_url
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

env = environ.Env()
environ.Env.read_env(Path.joinpath(BASE_DIR, '.env'))

SECRET_KEY = env("SECRET_KEY")
DEBUG = True
ALLOWED_HOSTS = [env('HOST_URL'),"localhost"]

# Application definition
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.sites",
    "allauth",
    "allauth.account",
    "allauth.socialaccount",
    "allauth.socialaccount.providers.google",
    "voting.apps.VotingConfig",
    "import_export",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "horc_elections.middleware.LoginRequiredMiddleware",
]

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [Path.joinpath(BASE_DIR, "templates")],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

ROOT_URLCONF = "horc_elections.urls"

WSGI_APPLICATION = "horc_elections.wsgi.application"

DATABASES = {
    "local": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    },
    "heroku": dj_database_url.config(),
}

default_database = env('DJANGO_DATABASE', default='local')
DATABASES['default'] = DATABASES[default_database]

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/
LANGUAGE_CODE = "en-us"
TIME_ZONE = "Asia/Kolkata"
USE_I18N = True
USE_TZ = True

SOCIALACCOUNT_PROVIDERS = {
    "google": {
        "SCOPE": [
            "profile",
            "email",
        ],
        "AUTH_PARAMS": {
            "access_type": "online",
            "prompt": "select_account",
        },
        "APP": {
            "client_id": env('GOOGLE_OAUTH_CLIENT_ID'),
            "secret": env('GOOGLE_OAUTH_SECRET'),
            "key": env('GOOGLE_OAUTH_KEY'),
        },
    }
}

AUTHENTICATION_BACKENDS = (
    "django.contrib.auth.backends.ModelBackend",
    "allauth.account.auth_backends.AuthenticationBackend",
)

SITE_ID = 3
LOGIN_URL = "/accounts/google/login/"
LOGIN_REDIRECT_URL = "/"
LOGIN_EXEMPT_URLS = ["/admin/*"]

IMPORT_EXPORT_USE_TRANSACTIONS = True

STATIC_URL = "static/"
STATICFILES_DIRS = [Path.joinpath(BASE_DIR, "static")]
STATIC_ROOT = Path.joinpath(BASE_DIR, "staticfiles/")
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"