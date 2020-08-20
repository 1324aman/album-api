# album-api
This project contains implementation of apis using django rest framework for simple album project.
We can display album list, photo list inside album.
Inside each album we can view photo list related to it.
We can add new photo, create new album .
# Technology Stack
We have used, 
Django, Django rest framework, and mysql database, Python 3.6
# Project Structure
─src
    ├───album
    │   ├───api
    │   │   └───__pycache__
    │   ├───migrations
    │   │   └───__pycache__
    │   └───__pycache__
    ├───album_project
    │   └───__pycache__
    ├───media
    │   └───album_images
    ├───static
    │   └───album
    │       └───images
    └───templates
        └───album

# Running Locally
clone the repository
git clone git@github.com:1324aman/album-api.git
Install the requirements 
pip install -r requirements.txt
Apply migrations
python manage.py migrate
Create admin
python manage.py createsuperuser
Run development server
python manage.py runserver
