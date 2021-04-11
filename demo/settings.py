# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '0c7216)gs^ne$%3+je20zuo+g0&^6yb@e68qdr!^!r0hmb-6y+'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = ["sso.paypalcorp.com", "sso.paypalcorp.com/idp/SSO.saml2", "https://psi_demonstrator.isro-nsc.papalcorp.com","psi_demonstrator.isro-nsc.papalcorp.com", "ssoqa.paypalcorp.com", "ssoqa.paypalcorp.com/idp/SSO.saml2", "0.0.0.0"]

# Application definition

INSTALLED_APPS = (
	"sslserver",
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)
MIDDLEWARE = MIDDLEWARE_CLASSES


ROOT_URLCONF = 'demo.urls'

WSGI_APPLICATION = 'demo.wsgi.application'



LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True



STATIC_URL = '/static/'

SAML_FOLDER = os.path.join(BASE_DIR, 'saml')

SESSION_ENGINE = 'django.contrib.sessions.backends.file'

#TEMPLATE_DIRS = (
#    os.path.join(BASE_DIR, 'templates'),
#)

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


CSRF_TRUSTED_ORIGINS =['https://sso.paypalcorp.com','sso.paypalcorp.com','https://sso.paypalcorp.com/idp/SSO.saml2','sso.paypalcorp.com/idp/SSO.saml2',"https://psi_demonstrator.isro-nsc.papalcorp.com","psi_demonstrator.isro-nsc.papalcorp.com",'https://ssoqa.paypalcorp.com','ssoqa.paypalcorp.com','https://ssoqa.paypalcorp.com/idp/SSO.saml2','ssoqa.paypalcorp.com/idp/SSO.saml2']

