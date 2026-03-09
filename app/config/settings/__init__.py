import os
import pathlib

from django.core.management.utils import get_random_secret_key

# Settings

MODE = os.getenv('MODE')

if MODE == 'development':
    from config.settings.development import *
elif MODE == 'ci':
    from config.settings.ci import *
else:
    from config.settings.main import *
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
        pathlib.Path(BASE_DIR / '..' / 'SECRET_KEY').write_text(SECRET_KEY)
    with pathlib.Path(BASE_DIR / '..' / 'SECRET_KEY').open('r') as file:
        SECRET_KEY = file.read().strip()


INSTALLED_APPS = TOP_PRIORITY_APPS + DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS + BOTTOM_PRIORITY_APPS
