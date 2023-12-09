. bin/activate
pip install -r requirements.txt

# Run migrations
python3.9 manage.py migrate
python3.9 manage.py runserver
