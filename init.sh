sudo rm /etc/nginx/sites-enabled/default
# sudo ln -sf /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/test.conf
sudo cp ./etc/nginx.conf /etc/nginx/sites-enabled/
sudo /etc/init.d/nginx restart

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