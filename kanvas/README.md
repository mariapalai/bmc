# Administration Guide

superuser/password: maria/maria
To rename the site, go to /admin at Sites section.
Sending email is enabled with the following instructions at the gmail of the admin:
https://support.google.com/accounts/answer/6010255

git checkout db.sqlite3
git pull
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py runserver 
visit: https://kanvas-mariapalai.c9users.io

Settings of a demo:
1. Locally, do not use an email to signup
2. At cloud9, do not signup and use a user with a confirmed email due to 
https://cloud.google.com/compute/docs/tutorials/sending-mail/

Tips for a demo:
1. As the email has to be unique, for testing you can use mailinator.
2. cloud9 hibernates its VM after 1-2 days of inactivity

