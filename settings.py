# coding: utf-8

from __future__ import unicode_literals
import os

import django


DATABASES = {
    'sqlite3': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'cachalot.sqlite3',
    },
    'postgresql': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'cachalot',
        'USER': 'cachalot',
        'HOST': 'localhost',
        'PORT': '5432',
    },
    'mysql': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'cachalot',
        'USER': 'root',
    },
}
for alias in DATABASES:
    test_db_name = 'test_' + DATABASES[alias]['NAME']
    if django.VERSION < (1, 7):
        DATABASES[alias]['TEST_NAME'] = test_db_name
    else:
        DATABASES[alias]['TEST'] = {'NAME': test_db_name}

DATABASES['default'] = DATABASES.pop(os.environ.get('DB_ENGINE', 'sqlite3'))


CACHES = {
    'locmem': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
    },
    'redis': {
        'BACKEND': 'redis_cache.cache.RedisCache',
        'LOCATION': '127.0.0.1:6379:0',
    },
    'memcached': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': '127.0.0.1:11211',
    },
}

CACHES['default'] = CACHES.pop(os.environ.get('CACHE_BACKEND', 'locmem'))


INSTALLED_APPS = [
    'cachalot',
    'django.contrib.auth',
    'django.contrib.contenttypes',
]
if django.VERSION < (1, 7):
    INSTALLED_APPS.append('south')


MIDDLEWARE_CLASSES = ()
PASSWORD_HASHERS = ('django.contrib.auth.hashers.MD5PasswordHasher',)
SECRET_KEY = 'it’s not important but we have to set it'