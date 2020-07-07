# setting up nginx
sudo rm -rf /etc/nginx/sites-enabled/*
sudo ln -sf /home/dean/web/etc/local_nginx.conf /etc/nginx/sites-enabled/nginx.conf
sudo /etc/init.d/nginx restart
# updating database
# rm -rf ~/web/ask/qa/migrate
python3 ~/web/ask/manage.py makemigrates
python3 ~/web/ask/manage.py 
# starting nginx
cd ask && gunicorn -c /home/dean/web/etc/gunicorn.conf.py ask.wsgi