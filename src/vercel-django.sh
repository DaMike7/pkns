pip install -r requirements.txt

# Run migrations
python3.9 manage.py migrate
python3.9 manage.py runserver
gunicorn pkns.wsgi:application -w 4 -k uvicorn.workers.UvicornWorker
