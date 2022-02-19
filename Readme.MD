## Commands:
- create project:
    - django-admin startproject project_name
- create app:
    - python3 manage.py startapp app_name
- run server:
    - python3 manage.py runserver
- create virtual environment:
    - virtualenv venv
- active virtual env:
    - . venv/bin/activate
- install required features:
    - write the features name in requirements.txt file
    - pip install -r requirements.txt
- table migration:
    - python3 manage.py migrate
- manual table migration:
    - first write the migration inside app/models.py file and then
    - python3 manage.py makemigrations app_name
- to see the tables which i migrated and geneated the migrations:
    - python3 manage.py sqlmigrate app_name 0001 (migration code)
- after chang or update models.py, run those cmd
    - python3 manage.py makemigrations app_name
    - python3 manage.py migrate
    - python3 manage.py sqlmigrate app_name 0001 (migration code)


## SQL commands:
- python3 manage.py shell
    - from WebApp.models import AllCourses, Details
    - from django.utils import timezone
    - import datetime
    - AllCourses.objects.filter(pk=1)
    - a=AllCourses.objects.get(pk=1)
    - a.was_published_recently()
    - a.details_set.all()
    - a.details_set.count()
    - a.details_set.create(course_type="Instructor Led")
- Create superuser:
    - python3 manage.py createsuperuser

## How to start writing test:
- /*identifying*/ the bug creating the projrct
- create test to /*expose*/ the bug
- running the test
- /*Fixing*/ the bug