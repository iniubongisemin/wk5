# INTRODUCTION TO DJANGO
# NB: in django, every wev app you create is called a project 
# django is a HLL python web framework that encourages rapid development and clean, pragmatic design and battery included philosophy
# OBJECT RELATIONAL MAPPING: a bridge between python and SQL for database management

#❎ ignore

# SETTING UP A DJANGO DEVELOPMENT ENVIRONMENT(DDE) (NB: in command prompt only)
# DDE consists of installing and setting up Python, Django and a Database System. 
# since django deals with web applications, you need a web server as well

# NB: THESE STEPS ARE FOR WHEN YOU'RE INSTALLING DDE FOR THE FIRST TIME

# 1. CREATE A FOLDER IN YOUR BACKEND 6B7 DIRECTORY THEN INSTALL THE VIRTUAL ENVIRONMENT SOFTWARE (PS: No need reinstall the virtual environment since you've already installed pip evironment software yesterday)
# pip install --upgrade pip OR pip install virtualenv ✅

# 2. CREATE A VIRTUAL ENVIRONMENT
# virtualenv yourenvironmentname ✅

# 3. MOVE INTO YOUR VIRTUAL ENVIRONMENT FOLDER VIA THE COMMANDLINE
# cd yourenvironmentname/scripts ✅

# 4. TO ACTIVATE YOUR VIRTUAL ENVIRONMENT
# activate ✅

# 5. INSTALL DJANGO
# pip install django==4.2.4 ✅

# 6. CHANGE DIRECTORY TO THE BASE FOLDER
# cd ../../ ✅

# 7. CREATE A DJANGO PROJECT
# django-admin startproject myproject ✅

# 8. NAVIGATE TO THE PROJECT DIRECTORY 
# cd myproject ✅

# 9. CREATE A NEW APP 
# python manage.py startapp myapp ✅

# 10. OPEN THE FILE IN VS CODE
# code . ✅

# 11. ADD THE APP TO INSTALLED_APPS LIST IN (settings.py)
# 'myapp.apps.MyAppConfig'✅

# 12. RUN THE DEVELOPMENT SERVER 
# python manage.py runserver ✅


# IF YOU ALREADY HAVE DDE INSTALLED AND HAVE A DJANGO PROJECT, FOLLOW THESE STEPS;
# 1. cd myproject

# 2. cd devenv

# 3. cd scripts

# 4. activate

# 5. cd ../../

# 6. cd myapp

# 7. code .

# 8. python manage.py runserver

# PS: to get a full list of commands accessible via manage.py, run;
# 9. python manage.py help


# with servers, there are two types of requests;
# 1. GET requests and
# 2. POST requests
    
# ACRONYMS
# TCP/IP: Transmission Control Protocol: communication protocols that define how data should travel across internet
# DNS: Domain Name System: its like an address for websites 
# HTTP: an application protocol that defines a language for clients and servers to speak to each other
# WSGI: Web Server Gateway Interface      

# Component files: 
# 1. Code files
# 2. Assets

# Checkout HTTP status codes
# 200 OK == 'status code for good request'

# Client initiated errors
# 400 OK == '   ''   ''     for bad request'
# 401 OK == 'status code for unauthorized request'
# 403 OK == '   ''   ''    for forbidden request'
# 404 OK == '   ''    ''  for not found'
# 405 OK == '   ''    ''   for unsupported HTTP method'

# Server initiated errors
# 50x 

# UPDATED STEPS
# 1. mkdir database_project ✅
# 2. cd database_project ✅
# 3. virtualenv appenv ✅
# 4. cd appenv/scripts ✅
# 5. - activate ✅ (for windows)
#    - source appenv/bin/activate (for mac) ✅
# 6. cd ../../ ✅
# 7. pip install django ✅
# 8. django-admin startproject myproject ✅
# 9. cd myproject ✅
# 10. python manage.py startapp mainapp ✅
# 11. register your app in settings.py file e.g 'mainapp.apps.MainappConfig' ✅
# 12. define your home, about, contact and xyz_page_views ✅
# 13. create a urls.py file in your app folder ✅  
# from django.urls import path
# from .views import home_page_view, about_page_view, contact_page_view, service_page_view

# urlpatterns = [
#     path('', home_page_view, name = 'home'),
#     path('about/', about_page_view, name = 'about'),
#     path('contact/', contact_page_view, name = 'contact'),
#     path('service/', service_page_view, name = 'service'),
# ]

# 14. include the link to your app.urls file in your django project's urls.py file ✅
# from django.contrib import admin
# from django.urls import path, include

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', include('hitechapp.urls'))
# ]

# 15. python manage.py makemigrations ✅
# 16. python manage.py migrate ✅
# 17. pyton manage.py shell ✅
# pip install pillow for image field
# go to settings.py and add MEDIA_URL= 'media/'
# MEDIA_ROOT=BASE_DIR / 'mediafiles'
# NB: in production DEBUG=True
# in urls.py:
# from django.conf import settings
# from django.conf.urls.static import static

# if settings.DEBUG:
    # urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# in views.py
# from .models import Post

def home_page_view(request):
    all_article = Post.objects.all()
    context = {
        'articles':all_article
    }
    return render(request, 'main/index.html', context)


# DATABASE 
# query == fetching or retrieving some info from a database
# Types of DB
# 1. Relational DB e.g of programming lang used, SQL: Structured Query Language
# e.g of SQLs: MySQL, PostgreSQL, Oracle, MariaDB,  
# 2. Non-Relational Database: They store their in an object structure i.e in key value pairs, or document, column-family, graphs
# e.g MongoDB, Google cloud firestore, Cassandra
# CRUD
# - Create
# - Read
# - Update
# - Delete

# whenever you make changes in your database, you must call the migration path
# every instance of a class you create represents a new record in the database
# you define your database table in the models.py file
# module: a file that contains code logic that can be imported 
# NB: when a file contains __init__.py it can be used and imported as a module
# in pure SQL, you must speccify what kind of datatype you want to store in a particular field
# django also has similar field functionality where you can specify the datatype to be stored in a particular field
# max_length is an attribute that is used to specify the maximum length of characters to be stored in a field NB: its a required attribute
# the null attribute is used to specify whether or not a particular field can be left blank
# if you're adding a new record and you want it to automatically record the time, set auto_now_add=True as an attribute of DateTimeField(when you're creating an existing record)
# if you're adding updating an existing record and you want it to take not automatically, set auto_now=True
# blank=True indicates that a value can be omitted when sending data to the database that already has a null=True attribute
# NB: You can manage your database table from the admin panel 
# ordering implies how the data should be ordered NB: by default it uses ascending order

# MIGRATION PROCESS
# 1. python manage.py makemigrations
# 1. python manage.py makemigrations yourapp (to ensure you directly target the app that you want to make migration)

# primary key field is used for indexing
# when you delete a row, the row is rendered useless for SQL DB 
# Queryset: a list of records/objects from your database
# Model instance: one single item from your database

# Using the model manager create method
# 1. 
# Model class save method 

# NB: when using the get() your lookup field must have a unique value
# id and primary key are one and same
# checkout the django documentation always!

 