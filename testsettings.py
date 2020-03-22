DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
    },
}

INSTALLED_APPS = (
    'django.contrib.contenttypes',
    'django.contrib.auth',
    'rest_framework.authtoken',
    'familiar',
)

ROOT_URLCONF = 'familiar.tests'

SECRET_KEY = 'test'

SETTING_VERSION = 4
