# Makefile

VIRTUALENV = venv/

run:
	. $(VIRTUALENV)bin/activate; export PYTHONPATH=`pwd`/app/:$(PYTHONPATH) ; python -W ignore::DeprecationWarning manage.py runserver 0.0.0.0:8000

install: create_virtualenv pip_install setup_db bower_install

create_virtualenv:
	# Check if venv folder is already created and create it
	if [ ! -d venv ]; then virtualenv $(VIRTUALENV) --no-site-package --distribute --prompt=Dystopia-Tracker; fi

pip_install:
	# Install pip dependencies
	. $(VIRTUALENV)bin/activate; pip install -r requirements_core.txt

npm_install:
	# Install npm packages
	if [ -s npm_requirements.txt ]; then xargs -a npm_requirements.txt npm install -g; fi

bower_install:
	bower install

setup_db:
	# setup database
	. $(VIRTUALENV)bin/activate; python manage.py syncdb --noinput; . $(VIRTUALENV)bin/activate; python manage.py migrate --all