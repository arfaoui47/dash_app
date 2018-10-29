from fabric.api import task, run, cd, hosts, sudo


#TODO add host server IP address
HOST = ""
#TODO add git REPO
GIT_REPO = ""


@task
@hosts(HOST)
def update_create_user():
    sudo("sudo apt-get update")
    sudo("sudo apt-get install python3-pip python3-dev nginx")
    sudo("sudo -H pip3 install virtualenv")

    sudo("adduser dash")
    sudo("usermod -aG sudo dash")
    sudo("su - dash")


@task
@hosts()
def deploy():
    run("git clone {}".format(GIT_REPO))
    run("cd ~/dash_app")
    run("virtualenv venv")
    run('venv/bin/pip install -r requirements.txt')
    sudo('systemctl start dash_app')
    sudo('systemctl enable dash_app')
