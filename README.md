# Provisioning

move to dash app directory:

```
virtualenv venv
venv/bin/pip install -r requirements.txt
```

Update scripts with GIT repos and server IP address:

```
source venv/bin/activate
fab -f  provision.py create_user
```

Create dash_app service script and copy dash_app.service code there.

```
sudo vi /etc/systemd/system/dash_app.service

```

Start the service and deploy app

```
fab -f  provision.py deploy
```