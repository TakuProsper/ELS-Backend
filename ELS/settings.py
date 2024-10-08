"""
Django settings for ELS project.
"""

from pathlib import Path
import os
from datetime import timedelta
from dotenv import load_dotenv

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Load environment variables
load_dotenv()

# Environment settings
ENVIRONMENT = os.environ.get('ENVIRONMENT', 'development')
POSTGRES_LOCALLY = os.environ.get('POSTGRES_LOCALLY', 'False') == 'True'

# Quick-start development settings - unsuitable for production
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', 'django-insecure-l#o2o72147o#6x13fl*evmoe#4gbhw_*!of06e6+83)&dj*v&)')
DEBUG = os.environ.get('DEBUG', 'False') == 'False'
ALLOWED_HOSTS = ['*']
CSRF_TRUSTED_ORIGINS = ['https://web-production-6cb9.up.railway.app']

# Application definition
INSTALLED_APPS = [
    'jazzmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'users.apps.UsersConfig',  # Make sure to use the app config
    'events',
    'rest_framework',
    'corsheaders',
    'rest_framework_simplejwt',
    'rest_framework_simplejwt.token_blacklist',
]

# Fixed middleware configuration
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',  # Required for admin
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',  # Required for admin
    'django.contrib.messages.middleware.MessageMiddleware',  # Required for admin
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'ELS.urls'

# Fixed templates configuration
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'ELS.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
import dj_database_url
database_url = os.environ.get("DATABASE_URL")
DATABASES["default"] = dj_database_url.parse(database_url)
#postgresql://els_user:5Hfpnlqduy5EoCoyRMvaFZu3rjTG4jQ4@dpg-cs2rvle8ii6s738bb9rg-a.oregon-postgres.render.com/els

# Custom User Model
AUTH_USER_MODEL = 'users.CustomUser'

# Password validation
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
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Static files configuration
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# CORS configuration
CORS_ORIGIN_ALLOW_ALL = True

# Rest Framework configuration
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    )
}

# JWT Settings
SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=5),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=50),
    'ROTATE_REFRESH_TOKENS': True,
    'BLACKLIST_AFTER_ROTATION': True,
    'UPDATE_LAST_LOGIN': False,
    'ALGORITHM': 'HS256',
    'AUTH_HEADER_TYPES': ('Bearer',),
}

# Email configuration
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER', 'takueprosper00@gmail.com')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD', 'prnksdygqbmnwnjr')

# Payment gateway configuration
PESEPAY_API_KEY = os.environ.get('PESEPAY_API_KEY', '2fc1978431b434e4993a88a4d44e795f')
PESEPAY_MERCHANT_ID = os.environ.get('PESEPAY_MERCHANT_ID', 'cdf9a77f-7348-4654-ad5a-11609b5672a7')
PESEPAY_API_URL = os.environ.get('PESEPAY_API_URL', 'https://api.pesepay.com/api/payments-engine/v1/payments/initiate')