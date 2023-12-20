#add
INSTALLED_APPS = [  
    'productlist.apps.ProductlistConfig',
    'rest_framework',
    'corsheaders',
]

MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",
]

CORS_ALLOW_ALL_ORIGINS = True
