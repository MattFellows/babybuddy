from .base import *

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

SECRET_KEY = 'CHANGE ME'
DEBUG = True


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'babybuddy',
        'USER': 'postgres',
        'PASSWORD': 'postgres01',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.StaticFilesStorage'


# Django Rest Framework
# http://www.django-rest-framework.org/#

REST_FRAMEWORK['DEFAULT_RENDERER_CLASSES'] = (
    'rest_framework.renderers.JSONRenderer',
    'rest_framework.renderers.BrowsableAPIRenderer',
)

BABY_BUDDY['ALLOW_UPLOADS'] = True
BABY_BUDDY['AWS_ACCESS_KEY_ID'] = 'AKIAJXAZYJ6YMJNLBEVA'
BABY_BUDDY['AWS_SECRET_ACCESS_KEY'] = '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'
BABY_BUDDY['AWS_STORAGE_BUCKET_NAME'] = 'baby-buddy'

AWS_ACCESS_KEY_ID = 'AKIAJXAZYJ6YMJNLBEVA'
AWS_SECRET_ACCESS_KEY = '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'
AWS_STORAGE_BUCKET_NAME = 'baby-buddy'

DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
