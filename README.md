# Library-App

Django-based webapp, used to display and manage books in library digitaly to
users and admin.

## Overview

* Language: Python (version:3)
* Platform: Windows / Ubuntu
* Framework: Django

### 1. Create python3 virtual environment and install requirements.txt
    `py -m venv <env>`
    `pip install django`
    `pip install pipreqs`
    `pipreqs location`

### 2. Performing Django Migrations
    Follow the below commands..
    `python3.6 manage.py makemigrations`
    `python3.6 manage.py migrate`

### 3. How to run
    Follow the below commands..
    `python3.6 manage.py runserver`

### 4. For testing APIs
`add admins using sign up API giving username and password`
`Admin password after creation, will be stored in db encrypted using sha256.`
`There are 6 html files in templates folder base dir used to display frontend.`
`There are 7 APIs for different purposes like create,delete,retrieve for admins,
retrive for users, sign  up etc.`
`home.html is the base html for all other html files.`
`Used forms.py for form field defenitions and used models for table creation.`
