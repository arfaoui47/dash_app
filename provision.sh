#!/usr/bin/env bash

sudo apt-get update
sudo apt-get install python3-pip python3-dev nginx git nodejs npm
sudo npm install -g localtunnel
sudo pip3 install virtualenv

#sudo adduser dash
#sudo usermod -aG sudo dash
#sudo su - dash

git clone git@github.com:arfaoui47/dash_app.git
cd ~/dash_app
virtualenv venv
venv/bin/pip install -r requirements.txt

# create dash_app service in /etc/systemd/system/dash_app.service
# create nginx config /etc/nginx/sites-available/dash_app
# link nginx config


# start web app service
#sudo systemctl start dash_app
#sudo systemctl enable dash_app
#
## restart nginx service
#sudo service nginx restart


venv/bin/gunicorn --bind 0.0.0.0:4041 web_app:server
lt --port 4041
