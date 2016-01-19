# Administration Guide

superuser/password: maria/maria

cloud9 hibernates its VM after one week of inactivity
cloud9 has Python 2.7.6 and Django 1.8.3

Developer Manual:

git pull # in case of conflicts with a file x, run 'git checkout x'
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py runserver 
visit: https://kanvas-mariapalai.c9users.io
To rename the site, go to /admin at Sites section.

Before using cloud9, make sure that you have users as you cannot signup from cloud9:
https://cloud.google.com/compute/docs/tutorials/sending-mail/

A the email has to be unique, for testing you can use mailinator.

Sending email is enabled with the following instructions at the gmail of the admin:
https://support.google.com/accounts/answer/6010255

To visualize dependencies between kanvas modules and django modules, install snakefood and type:
sfood -I migrations . | sfood-graph | dot -Tsvg > x.svg

