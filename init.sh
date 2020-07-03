# updating django
sudo pip3 install --upgrade django==2.0.7
# installing crispy for nice-forms
pip install update
pip install django-crispy-forms
# setting nginx
sudo ln -sf /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/test.conf
sudo rm -rf /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart
# setting mysql database
sudo /etc/init.d/mysql start
mysql -uroot -e "create database web;"
mysql -uroot -e "grant all privileges on web.* to 'box'@'localhost' with grant option;"
# reinitializing database
rm -rf ~/web/ask/qa/migrate
python3 ~/web/ask/manage.py makemigrates
python3 ~/web/ask/manage.py migrate
python3 ~/web/ask/manage.py createsuperuser
# starting gunicorn. (never works. have to do it by hands)
# cd /home/box/web/ask && gunicorn -c /home/box/web/etc/gunicorn.conf.py ask.wsgi
