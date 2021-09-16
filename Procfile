release: python manage.py migrate
web: daphne fastparcel.asgi:application -p $PORT -b 0.0.0.0 -v2
web: gunicorn fastparcel.wsgi