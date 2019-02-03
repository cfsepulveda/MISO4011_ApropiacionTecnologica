release: python manage.py createsuperuser
release: python manage.py migrate
web: gunicorn agileProject.wsgi --log-file -
