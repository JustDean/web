# updating django
sudo pip3 install --upgrade django==2.0.7
# setting nginx 
sudo ln -sf /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/test.conf
sudo rm -rf /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart
# setting mysql database
sudo /etc/init.d/mysql start
mysql -uroot -e "create database web;"
mysql -uroot -e "grant all privileges on web.* to 'box'@'localhost' with grant option;"
# follow next steps after changing user in ask/settings 
# rm -rf ~/web/ask/qa/migrate
# python3 ~/web/ask/manage.py makemigrates
# python3 ~/web/ask/manage.py migrate
# # starting gunicorn
cd /home/box/web/ask && gunicorn -c /home/box/web/etc/gunicorn.conf.py ask.wsgi