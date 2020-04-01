# Transcendence project

This is initial version of the final Devman project.
It has following features:

- view for reviewing users (`/users/123/`).
- usage of django-configurations package.
- usage of Sentry.

Prior to start, install the requirements:

    pip install -r requirements.txt
    
Then run

    python manage.py migrate --settings=transcendence.settings --configuration=Dev
    python manage.py runserver --settings=transcendence.settings --configuration=Dev

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
