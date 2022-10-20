# django_rest
Init Django Rest Framework 

# Create project
django-admin startproject django_rest

# path to project folder
cd django_rest

# Create apps
django-admin startapp user_app

django-admin startapp catalog_app

pip install -r requirements.txt

# Create migrations standard
python manage.py makemigrations
# if migrations a app detail, example user_app
python manage.py makemigrations user_app

# Apply into DB
python manage.py migrate
# if migrate a app detail, example user_app
python manage.py migrate user_app

# Create account admin
python manage.py createsuperuser

# if using port default 8000
python manage.py runserver
# if using port other, ex 8083
python manage.py runserver localhost:8083

# Run on browser
http://localhost:8083/

# Run user
http://localhost:8083/user/

# Run admin site
http://localhost:8083/admin/

# if APIs
http://localhost:8083/user/all-accounts

