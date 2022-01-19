# testove_2
Flask based app that greets a user. If it's a new user the program says "Hello" and if the user is already in the db it says "Hello again". It also has a button where it shows all known users.

Getting Started
pip install virtualenv

git clone https://github.com/HlazL/testove_2.git

pip install -r requirements.txt

To run locally:
type into the terminal:

export FLASK_APP=application.py FLASK_ENV=development && flask run