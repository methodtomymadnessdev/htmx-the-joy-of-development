# HTMX bringing back the joy of development
This is a demo application aimed at showing you how to use HTMX. To read the full article please visit [methodtomymadness.dev/htmx-bringing-back-the-joy-of-development/](methodtomymadness.dev/htmx-bringing-back-the-joy-of-development/)

## Setup
1. You'll need to clone it and create a virtual environment.

```bash
# create a virtual environment
python3 -m virtualenv venv

# if you don't have virtualenv
python3 -m pip install virtualenv

# activate the environment
source venv/bin/activate

# install dependencies
python3 -m pip install -r requirements.txt

# run migration
python3 manage.py migrate

# create superuser
python3 manage.py createsuperuser

# Runserver
python3 manage.py runserver
```

2. Navigate to http://localhost:8000

Thanks it!

