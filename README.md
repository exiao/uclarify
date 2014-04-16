uclarify
========

uClarify

Initial Setup
pip install virtualenvwrapper

virtualenv env

source ./env/bin/activate

pip install -r requirements.txt

./dev

MIGRATIONS
./manage.py schemamigration ucapp --initial
./manage.py schemamigration ucapp --auto
./manage.py migrate
