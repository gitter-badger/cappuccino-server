#! /bin/bash

# TODO:
# Most of this command could be defined in the README.md
# to let users keep the control of the installation!
DATABASE_NAME="cappuccino"

# Installing Virtualenv
echo -e "Installing virtualenv ..."
pip install virtualenv

# Creating and Activating Virtualenv
echo -e "Creating new Virtual Environment ..."
virtualenv env
source env/bin/activate

# Installing Web Client
# TODO: Ugly.. maybe a git submodule could be a good idea
echo -e "Cloning Cappuccino-Web ..."
#git clone git@github.com:cappuccino-app/cappuccino-web.git
wget https://github.com/cappuccino-app/cappuccino-web/archive/master.zip
unzip master.zip
mv cappuccino-web-master cappuccino-web

# Installing Django pip requirements
echo -e "Installing PIP requirements ..."
pip install -r requirements-python2.7.txt

# Creating Static Files Directory for django
echo -e "Creating Static Files Directory ..."
# TODO: Rename owndrive to cappuccino
mkdir -p owndrive/static

# Collecting Static Files for serving Web Client Resources
echo -e "Collecting Static Files ..."
python manage.py collectstatic --no-input

# Creating MySql database
# TODO: Re-Enable it later!
echo -e "Creating MySql Database ..."

if [ $1 == "--test" ]
	then
		mysql -u root -e "CREATE DATABASE IF NOT EXISTS $DATABASE_NAME"

		# Making Migrations
		echo -e "Applying Migrations ..."
		python manage.py migrate
	else
		echo "Choose MySql Password [ENTER]: "
		read PASSWD
		mysql -u root -e "CREATE DATABASE IF NOT EXISTS $DATABASE_NAME"	-p$PASSWD

		# Setting Password inside local_settings.py
		sed -i "s/'PASSWORD': '',/'PASSWORD': '$PASSWD',/g" owndrive/local_settings.py

		# Making Migrations
		echo -e "Applying Migrations ..."
		python manage.py migrate

		# Creating Super User
		echo -e "Creating Super User for Cappuccino-App ..."
		python manage.py createsuperuser --username=admin_user --email=admin@cappuccino.com
fi
