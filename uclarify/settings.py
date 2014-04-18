"""
Django settings for uclarify project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'i4f56&*xgbf#r=_fluce!dixx@xyis^0d%1+-#-37^@y3m=-i='

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

DEFAULT_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
)

LOCAL_APPS = (
    'ucapp',
    'li_registration',
)

THIRD_PARTY_APPS = (
    'static_precompiler',
    'south',
    'haystack',
    'social.apps.django_app.default',
    'registration',
    'registration_email',
)


INSTALLED_APPS = DEFAULT_APPS + LOCAL_APPS + THIRD_PARTY_APPS

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'uclarify.urls'

WSGI_APPLICATION = 'uclarify.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'

STATIC_ROOT = BASE_DIR + '/static/'
#STATIC_PRECOMPILER_ROOT = BASE_DIR + "/static/"
#STATIC_PRECOMPILER_OUTPUT_DIR = "COMPILED"

STATIC_PRECOMPILER_COMPILERS = (
  #"static_precompiler.compilers.CoffeeScript",
  #"static_precompiler.compilers.SASS",
  'static_precompiler.compilers.SCSS',
  #"static_precompiler.compilers.LESS",
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    # other finders..
    'static_precompiler.finders.StaticPrecompilerFinder',
)

TEMPLATE_DIRS = (
    BASE_DIR + '/templates/',
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

DJANGORESIZED_DEFAULT_SIZE = [1024, 768]

HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.elasticsearch_backend.ElasticsearchSearchEngine',
        'URL': 'http://127.0.0.1:9200/',
        'INDEX_NAME': 'haystack_uclarify',
    },
}

import django.conf.global_settings as DEFAULT_SETTINGS

TEMPLATE_CONTEXT_PROCESSORS = DEFAULT_SETTINGS.TEMPLATE_CONTEXT_PROCESSORS + (
    'social.apps.django_app.context_processors.backends',
    'social.apps.django_app.context_processors.login_redirect',
    'django.core.context_processors.request',
)

################## EMAIL STUFF ##########################
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.sendgrid.net'
EMAIL_HOST_USER = 'buynearme'
EMAIL_HOST_PASSWORD = 'CalClassified'
EMAIL_PORT = 587

#TEMPLATED_EMAIL_TEMPLATE_DIR = BASE_DIR + '/templates/email/'
#TEMPLATED_EMAIL_BACKEND = 'templated_email.backends.vanilla_django'

################## SOCIAL STUFF #########################
ACCOUNT_ACTIVATION_DAYS = 7

AUTHENTICATION_BACKENDS = (
    'social.backends.linkedin.LinkedinOAuth',
    'registration_email.auth.EmailBackend',
    'django.contrib.auth.backends.ModelBackend',
)
SOCIAL_AUTH_LINKEDIN_SCOPE = ['r_basicprofile', 'r_emailaddress']

SOCIAL_AUTH_LINKEDIN_FIELD_SELECTORS = [
    'email-address',
    'headline', # The job title
    'industry',
    'positions', # Used to retrieve the company
]

SOCIAL_AUTH_PROTECTED_USER_FIELDS = ['email', 'name']

SOCIAL_AUTH_LINKEDIN_EXTRA_DATA = [
    ('id', 'id'),
    ('first-name', 'first_name'),
    ('last-name', 'last_name'),
    ('email-address', 'email_address'),
    ('headline', 'headline'),
    ('industry', 'industry'),
    ('positions', 'positions')]

SOCIAL_AUTH_LINKEDIN_KEY = '75enltnahdhfvf' # The LinkedIn application "API Key"
SOCIAL_AUTH_LINKEDIN_SECRET = 'qGwQ4DwtU6rfWD46' # The LinkedIn application "Secret Key"

LOGIN_URL = '/login/'
LOGIN_ERROR_URL = '/error/'
LOGIN_REDIRECT_URL = '/complete/'
REGISTRATION_EMAIL_REGISTER_SUCCESS_URL = '/complete/'

SOCIAL_AUTH_PIPELINE = (
    'social.pipeline.social_auth.social_details',
    'social.pipeline.social_auth.social_uid',
    'social.pipeline.social_auth.auth_allowed',
    'social.pipeline.social_auth.social_user',
    'social.pipeline.user.get_username',
    'social.pipeline.user.create_user',
    'social.pipeline.social_auth.associate_user',
    'social.pipeline.social_auth.load_extra_data',
    'social.pipeline.user.user_details',
    'li_registration.models.social_auth_to_profile'
)

AUTH_PROFILE_MODULE = 'li_registration.UserProfile'
#AUTH_USER_MODEL = 'ucapp.UserProfile'
#SOCIAL_AUTH_USER_MODEL = 'ucapp.UserProfile'