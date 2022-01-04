web: gunicorn loginPage.wsgi
release: python manage.py makemigrations --noinput
release: python manage.py collectstatics --noinput
release: python manage.py migrate --noinput
# web: python manage.py runserver 0.0.0.0:$PORT --noreload
