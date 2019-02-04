release: pip3 install django-cors-headers
release: python manage.py migrate
web: gunicorn agileProject.wsgi --log-file -
