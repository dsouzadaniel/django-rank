release: python3 manage.py migrate
release: python3 manage.py loaddata preload.json
web: gunicorn djangorank.wsgi --preload --log-file -