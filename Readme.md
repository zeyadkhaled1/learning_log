python -m venv environmentname(Making Virtual Environment)
environmentname\Scripts\activate (Activating Virtual Environment)
pip install django(Installing Django)
django-admin startproject projectname .(For Starting a new Project)
python manage.py migrate(For Creating Database for the first time)
python manage.py runserver (Running the server)
python manage.py startapp appname(Making a new app)
After Model Change:
python manage.py makemigrations appname
python manage.py migrate
For Making Superuser:python manage.py createsuperuser
