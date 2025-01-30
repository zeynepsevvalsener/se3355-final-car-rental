import os
from pathlib import Path
from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-CHANGE_THIS_TO_YOUR_OWN_SECRET_KEY'
DEBUG = True
ALLOWED_HOSTS = ['se3355-final-car-rental.onrender.com','127.0.0.1']



USE_L10N = True
USE_TZ = True


INSTALLED_APPS = [
    # Django Apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # django-allauth (Google OAuth vb.)
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',

    # Uygulamamız
    'MyApp.apps.MyAppConfig',
]

SITE_ID = 1

AUTHENTICATION_BACKENDS = (
    "django.contrib.auth.backends.ModelBackend",
    "allauth.account.auth_backends.AuthenticationBackend",
)

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    'allauth.account.middleware.AccountMiddleware',
    
]

ROOT_URLCONF = 'vehicles.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',  # allauth için kritik
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.i18n',
            ],
        },
    },
]

WSGI_APPLICATION = 'vehicles.wsgi.application'

# Veritabanı (varsayılan SQLite)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Parola Validasyonu (Django'nun default'u + min length vs.)
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
        'OPTIONS': {
            'min_length': 8
        }
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Dil Ayarları
LANGUAGE_CODE = 'tr'
LANGUAGES = [
    ('en', 'English'),
    ('tr', 'Türkçe'),
]
# i18n çeviri dosyaları
LOCALE_PATHS = [
     BASE_DIR / 'locale', 
]


USE_I18N = True

TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True



# Static ve Media
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

#
# django-allauth Google ayarları (örnek)
# (Kendi Client ID ve Secret'ınızı ekleyin)
#


# .env dosyasını yükle
load_dotenv()

SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'SCOPE': ['email', 'profile'],
        'AUTH_PARAMS': {'access_type': 'online'},
        'APP': {
            'client_id': os.getenv('446528386628-24ahh9puvsfod7nu5f8vqp1kabfh2q65.apps.googleusercontent.com'),
            'secret': os.getenv('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'),
            'key': ''
        }
    }
}

