# task 1
sudo rm -rf /etc/nginx/sites-enabled/*
sudo ln -sf /home/dean/web/etc/local_nginx.conf /etc/nginx/sites-enabled/nginx.conf
sudo /etc/init.d/nginx restart
#task 2
# gunicorn -c /home/dean/web/etc/gunicorn.conf.py /ask
#task 3
cd ask && gunicorn -c /home/dean/web/etc/gunicorn.conf.py ask.wsgi
#task 4
rm -rf ~/web/ask/qa/migrate
python3 ~/web/ask/manage.py makemigrates
python3 ~/web/ask/manage.py migrate