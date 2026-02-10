import os

from django.core.management.utils import get_random_secret_key

# Settings

MODE = os.getenv('MODE')

if MODE == 'development':
    from config.settings.development import *
# elif MODE == 'production':
#     from config.settings.production import *
# elif MODE == 'staging':
#     from config.settings.staging import *
# elif MODE == 'ci':
#     from config.settings.ci import *

# Secret key

SECRET_KEY = os.getenv('SECRET_KEY', '')
if not SECRET_KEY:
    if not (BASE_DIR / '..' / 'SECRET_KEY').exists():
        SECRET_KEY = get_random_secret_key()
        with open(BASE_DIR / '..' / 'SECRET_KEY', 'w') as file:
            file.write(SECRET_KEY)
    with open(BASE_DIR / '..' / 'SECRET_KEY', 'r') as file:
        SECRET_KEY = file.read().strip()


INSTALLED_APPS = TOP_PRIORITY_APPS + DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS + BOTTOM_PRIORITY_APPS
