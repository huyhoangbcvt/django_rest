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

http://localhost:8083/catalog/

# Run admin site
http://localhost:8083/admin/

# APIs
# Groups
http://localhost:8083/user/groups/

# Register
http://localhost:8083/user/sign-up/

# List users
http://localhost:8083/user/users/

# Register: djoser endpoints
http://localhost:8083/user/auth/users/

# Get token user
http://localhost:8083/user/get-token/

# Get refresh token & access token: djoser endpoints
http://localhost:8083/user/auth/jwt/create/

# Get refresh token & access token
http://localhost:8083/user/refresh-token/

# category list
http://localhost:8083/catalog/category/

# category add
http://localhost:8083/catalog/category/add/?role=Guess&username=it.hoanghh

# product list
http://localhost:8083/catalog/product/

# product add
http://localhost:8083/catalog/product/add/?role=Guess&username=it.hoanghh
