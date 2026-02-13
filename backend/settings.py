INSTALLED_APPS += ['corsheaders']
MIDDLEWARE = ['corsheaders.middleware.CorsMiddleware'] + MIDDLEWARE
CORS_ALLOWED_ORIGINS = ["https://your-frontend-url.com"]


import os
import dj_database_url

SECRET_KEY = os.getenv("SECRET_KEY")
DEBUG = os.getenv("DEBUG") == "True"
ALLOWED_HOSTS = [os.getenv("ALLOWED_HOSTS")]

# Database config
DATABASES = {
    'default': dj_database_url.parse(os.getenv('DATABASE_URL'))
}

# CORS
INSTALLED_APPS += ['corsheaders']
MIDDLEWARE = ['corsheaders.middleware.CorsMiddleware'] + MIDDLEWARE
CORS_ALLOWED_ORIGINS = [os.getenv("FRONTEND_URL")]
