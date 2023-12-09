. bin/activate
pip install -r requirements.txt

# Run migrations
python manage.py migrate
python manage.py runserver
