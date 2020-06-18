# task 1
sudo rm /etc/nginx/sites-enabled/local_nginx.conf 
sudo ln -sf /home/dean/web/etc/local_nginx.conf /etc/nginx/sites-enabled/
sudo /etc/init.d/nginx restart