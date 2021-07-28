# Ambient monitor

## Local development

Create a ptyon environment.
```
python3 -m venv .venv
. .venv/bin/activate
python pip install -r requirements.txt
```

Create `config/local_settings.py` for local development as below.
```python
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = <YOUR DJANGO SECRET KEY>

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False
```

Run Django on local.
```
python manage.py migrate
python manage.py collectstatic
python manage.py createsuperuser
heroku local
```
