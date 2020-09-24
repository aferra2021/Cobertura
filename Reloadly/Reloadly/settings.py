﻿"""
Django settings for Reloadly project.

Generated by 'django-admin startproject' using Django 3.0.6.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os
from django.urls import reverse_lazy


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'pw6#wa+2zk#s46y=gy3k#g8jjom*%(j(!j7x@4r5it4p*t%l5x'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
#TEMPLATE_DEBUG = DEBUG
#ALLOWED_HOSTS = ['127.0.0.1']


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    #'social_django',
    #LOCALES
    'apps.RecargasCubacel',
    'apps.RecargasNauta',
    'apps.EtecsaTelefonoFijo',
    'apps.CubacelTur',
    'apps.CubacelSimTelefono',
    'apps.ServiciosDing',
    'apps.Usuarios',
    'apps.MercadoPago',
    'apps.StripeAPI',
    #Social,(pip install rest-social-auth)
    'rest_framework',#facebook
    #'rest_framework.authtoken',  # only if you use token authentication
    'social_django',  # django social auth#facebook
    'rest_social_auth',  # this package#facebook
    #'knox',  # Only if you use django-rest-knox
    #'rest_framework_social_oauth2',
    #'oauth2_provider',
    #'social_django',
    #'rest_framework_social_oauth2',
    'social.apps.django_app.default',#google
    #'xauth',#autentication with ajax
    'six',
    #sweetAlert
    'sweetify'

]
# Application definition


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'Reloadly.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'Templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
           #SOCIAL
                'social.apps.django_app.context_processors.backends',
                'social.apps.django_app.context_processors.login_redirect',
            ],
        },
    },
]


WSGI_APPLICATION = 'Reloadly.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

#stripe
#STRIPE_SECRET_KEY = config('sk_test_4eC39HqLyjWDarjtT1zdp7dc')
STRIPE_PUBLISHABLE_KEY  =  'sk_test_4eC39HqLyjWDarjtT1zdp7dc'
STRIPE_SECRET_KEY ='sk_test_4eC39HqLyjWDarjtT1zdp7dc'

#SOCIAL
AUTHENTICATION_BACKENDS = (
    'social_core.backends.facebook.FacebookOAuth2',
    # and maybe some others ...
    'django.contrib.auth.backends.ModelBackend',

    'social.backends.google.GoogleOpenId',
    'social.backends.google.GoogleOAuth2',
    'social.backends.google.GoogleOAuth',
)
# Facebook configuration
SOCIAL_AUTH_FACEBOOK_KEY = '1145973509113022'
SOCIAL_AUTH_FACEBOOK_SECRET = '815b1f38b4a08d84181c2493f0dd9175'
#google
SOCIAL_AUTH_GOOGLE_OAUTH2_KEY='837556477234-btgu807muqsgk3mcfards8hi8df0kbot.apps.googleusercontent.com'
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET ='FtbKUYA5XEpgcQEd6xjEBMxw'
REST_SOCIAL_DOMAIN_FROM_ORIGIN=True
SOCIAL_AUTH_LOGIN_REDIRECT_URL='/cobertura/'
REST_SOCIAL_OAUTH_REDIRECT_URI = 'cobertura'
REST_SOCIAL_OAUTH_ABSOLUTE_REDIRECT_URI = 'http://http://127.0.0.1:8000/cobertura/'
REST_SOCIAL_LOG_AUTH_EXCEPTIONS=True
SOCIAL_AUTH_STRATEGY='rest_social_auth.strategy.DRFStrategy'
#end SOCIAL

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'

LOGIN_REDIRECT_URL = reverse_lazy('cobertura')
LOGOUT_REDIRECT_URL = reverse_lazy('cobertura')

#recuperacion de contraseñas
EMAIL_BACKEND='django.core.mail.backends.smtp.EmailBackend'
#EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'aferra444'
EMAIL_HOST_PASSWORD = '97091602468'
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = 'aferra444@gmail.com'

#sweetAlert2
SWEETIFY_SWEETALERT_LIBRARY = 'sweetalert2'


STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'),)