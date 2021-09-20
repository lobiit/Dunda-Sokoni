"""
Django settings for fastparcel project.

Generated by 'django-admin startproject' using Django 3.1.3.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'f88mj#!)pv2_jx8d^58+roz4rv2fuhx!@n7%7#lo$6fgy@(h&v'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*', ]

# Application definition

INSTALLED_APPS = [
    'admin_interface',
    'colorfield',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'bootstrap4',
    'social_django',
    'core.apps.CoreConfig',
    'channels',

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'core.middleware.ProfileMiddlware',
]

ROOT_URLCONF = 'fastparcel.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'social_django.context_processors.backends',
                'social_django.context_processors.login_redirect',
            ],
        },
    },
]

WSGI_APPLICATION = 'fastparcel.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'FastParcel',
        'USER': 'postgres',
        'PASSWORD': 'Pythondev12!?',
        'HOST': 'localhost'
    }
}

# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

STATIC_URL = '/static/'
STATIC_ROOT = 'staticfiles'

LOGIN_URL = '/sign-in/'
LOGIN_REDIRECT_URL = '/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

AUTHENTICATION_BACKENDS = (
    'social_core.backends.facebook.FacebookOAuth2',
    'django.contrib.auth.backends.ModelBackend',
)

SOCIAL_AUTH_FACEBOOK_KEY = "1041448706391897"
SOCIAL_AUTH_FACEBOOK_SECRET = "ae5bea4d64b6ea01fb6f6150d3ff781f"
SOCIAL_AUTH_FACEBOOK_SCOPE = ['email']
SOCIAL_AUTH_FACEBOOK_PROFILE_EXTRA_PARAMS = {
    'fields': 'id, name, email'
}

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER = 'johnlobiit@gmail.com'
EMAIL_HOST_PASSWORD = 'Pythondev12!?'
DEFAULT_FROM_EMAIL = 'firebase-adminsdk-5txsn@undwa-c6f43.iam.gserviceaccount.com'

FIREBASE_ADMIN_CREDENTIAL = os.path.join(BASE_DIR, "undwa-c6f43-firebase-adminsdk-5txsn-b2ad517789.json")

STRIPE_API_PUBLIC_KEY = "pk_test_51JY8imKpY7UFqkDbWBrlWbmG2R8CGhANPRhOVPhNIJYRcuMea7v4L10VLfVuRiMRBcO63JmIhKmbwjkEB2k5UOSg00gvadj47E"
STRIPE_API_SECRET_KEY = "sk_test_51JY8imKpY7UFqkDb25pbQ0SbHsnRXZq4C5Z0OEP4z66vQWMySppMJVwLvenzKA2ciSJo8i83W1eyDPi4gWck2rC200CuqES3Rq"

GOOGLE_MAP_API_KEY = "AIzaSyAPR3Bc59b59Vjh0o12HEIaLf9ZvpfUQcE"

PAYPAL_MODE = "sandbox"
PAYPAL_CLIENT_ID = "YOUR_PAYPAL_CLIENT_ID"
PAYPAL_CLIENT_SECRET = "YOUR_PAYPAL_CLIENT_SECRET"

NOTIFICATION_URL = "https://dunda-sokoni.herokuapp.com/"

ASGI_APPLICATION = "fastparcel.asgi.application"

# Channels
CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels_redis.core.RedisChannelLayer',
        'CONFIG': {
            "hosts": ['YOUR_HEROKU_REDIS_URL'],
        },
    },
}

# Activate Django Heroku
import django_heroku

django_heroku.settings(locals())
