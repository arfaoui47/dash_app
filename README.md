# Provisioning

move to dash app directory:

```
virtualenv venv
venv/bin/pip install -r requirements.txt
```

Update scripts with GIT repos and server IP address in provision.py.
Run the following command to install dependencies in server and create new user: 
```
source venv/bin/activate
fab -f  provision.py create_user
```

Create dash_app service script and copy dash_app.service code there.

```
sudo vi /etc/systemd/system/dash_app.service

```

Create an NGINX config in `/etc/nginx/sites-available/dash_app` and copy `nginx.conf` there,
then link the file to the sites-enabled directory:
```
sudo ln -s /etc/nginx/sites-available/dash_app /etc/nginx/sites-enabled
```

Start the service and deploy app

```
fab -f  provision.py deploy
```

# Deployment

```
fab -f  deployment.py deploy
```
