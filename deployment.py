from fabric.api import task, run, cd, hosts, sudo

HOST = ""
#TODO add git REPO
GIT_REPO = ""

@hosts(HOST)
def deploy():
	with cd('/home/dash/dash_app/'):
		run('git pull')
		run('venv/bin/pip install -r requirements.txt')


	sudo('service nginx restart')

