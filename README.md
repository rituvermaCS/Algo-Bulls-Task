## Algo-Bulls-Task using Django REST framework

# Main points for creating a REST API in Django.

 find out steps to creating a REST API.

    Set-Up Virtual Environment.
    Set-Up Django
    Create a model for the database that the Django ORM will manage.
    Set-Up Django Rest Framework
    Serialize the model data from step-3
    Create the URI endpoint to view the serialized data.

# 1. Set-Up Virtual Environment

sudo apt update

sudo apt install python3-django

sudo apt install python3-pip

sudo apt install python3-venv

mkdir Algo-Bulls-Task

cd Algo-Bulls-Task

python3.6 -m venv aenv

source aenv/bin/activate

# 2. Set-Up Django

pip install django

django-admin startproject ToDo

# Check Django Server is working properly or not

python manage.py runserver

# Creating the app

python manage.py startapp api

# Migrate the database

python manage.py makemigrations

python manage.py migrate

# Create Super User

python manage.py createsuperuser

python manage.py runserver

# 3.Set-Up the Django Rest Framework

pip install djangorestframework

python manage.py runserver

# Root Path for localhost

Read all existing data: http://127.0.0.1:8000/api/read-all/

Read one existing data by ID reference: http://127.0.0.1:8000/api/read-one/id/

Update an existing data by ID reference: http://127.0.0.1:8000/api/update/id/

Create new data information: http://127.0.0.1:8000/api/create/

Delete existing data by ID reference: http://127.0.0.1:8000/api/delete/id
