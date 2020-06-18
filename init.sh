#task 1
sudo ln -sf /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/test.conf
sudo rm -rf /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart
#task 2
# gunicorn -c /home/box/web/etc/gunicorn.conf.py hello:app
#task 3
sudo pip3 install --upgrade django==2.0.7
cd /home/box/web/ask && gunicorn -c /home/box/web/etc/gunicorn.conf.py ask.wsgi

# sudo /etc/init.d/nginx restart
# sudo /etc/init.d/mysql start
# mysql -uroot -e "create database stepic_web;"
# mysql -uroot -e "grant all privileges on stepic_web.* to 'box'@'localhost' with grant option;"
# sudo pip3 install --upgrade django==2.0.7

# tip: change settings.py - set different default database

# then apply as following:
# rm -rf ~/web/ask/qa/migrate
# python3 ~/web/ask/manage.py makemigrates
# python3 ~/web/ask/manage.py migrate