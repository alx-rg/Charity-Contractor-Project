
# env/bin/activate
# If you ever want to deactivate your virtual environment, just type deactivate in your terminal window.#
# export FLASK_ENV=development; flask run
# http://127.0.0.1:5000/
# localhost:5000

# MongoDB 
# brew services start mongodb-community@5.0 
# Verify that it's running with : brew services list
# to stop MongoDB brew services stop mongodb-community@5.0
# 

from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient
from bson.objectid import ObjectId
import os

"""
import os
# pip install dnspython
# pip3 install certifi
import certifi
# Info from wd3.myworkday.com/shopify/d/home.htmld and https://medium.com/analytics-vidhya/deploy-a-web-api-with-python-flask-and-mongodb-on-heroku-in-10-mins-71c4571c505d

ca = certifi.where()
app = Flask(__name__)
host = os.environ.get('MONGODB_URI') 
DATABASE_URL = f'mongodb+srv://alexross:{os.environ.get("password")}@cluster0.c3gdz.mongodb.net/Cluster0?retryWrites=true&w=majority'

client = MongoClient(DATABASE_URL, tlsCAFile=ca)
"""
#host = os.environ.get("DB_URL")
client = MongoClient(host=host)
db = client.CharityTracker
charities = db.charities
users = db.users
donations = db.donations


#create instance of the flask server (Server:Flask)
#as the root directory within 'main.py'
app = Flask(__name__)

# create some routes!
# Anytime I want to interact with the SERVER FLASK I have to reference the "app" variable
# the @ is a python DECORATOR
# The / is the DEFAULT slash
""" 
/users	        GET	        index	    See all users
/users/new	    GET	        new	      See new user form
/users	        POST	      create	  Create a new user
/users/:id	    GET	        show	    See one user
/users/:id/edit	GET	        edit	    See an edit user form
/users/:id	    PATCH/PUT	  update	  Update a user
/users/:id	    DELETE	    destroy	  Delete a user

/donations	        GET	        index	    See all donations      <----- MAYBE
/donations	        POST	      create	  Create a new donation
/donations/:id/edit	GET	        edit	    See an edit donation form
/donations/:id	    PATCH/PUT	  update	  Update a donation
/donations/:id	    DELETE	    destroy	  Delete a donation

MAYBE ITEMS TO DO:
/charities	        GET	        index	    See all charities
/charities/new	    GET	        new	      See new charity form
/charities	        POST	      create	  Create a new charity
/charities/:id	    GET	        show	    See one charity
/charities/:id/edit	GET	        edit	    See an edit charity form
/charities/:id	    PATCH/PUT	  update	  Update a charity
/charities/:id	    DELETE	    destroy	  Delete a charity
 """


# users = [
#     { 'name': 'Jim Corning', 'username': 'jCorn' },
#     { 'name': 'George Lucas', 'username': 'gLucas' }
# ]

# ONLY ALLOW THE WEBSITE TO DISPLAY (Drop Down) A CHARITY LISTED below (to start)
# TO DO - Allow user to enter a new charity, and once listed, allow to be chosen from drop down
# charities = [
#     { '_id': 1, 'name': 'Humane Society', 'impact': 10, 'info': 'Helps dogs find new homes, succesful 100%.'}, 
#     { '_id': 2, 'name': 'Dogs For Life', 'impact': 9, 'info': 'Dogs and wonderful families.'},
#     { '_id': 3, 'name': 'MooseDoodle Shelter', 'impact': 10, 'info': 'Shelter 4 dogs.'},
#     { '_id': 4, 'name': 'Green Peace Dogs', 'impact': 8, 'info': 'Saves dogs in the food trade.'},
#     { '_id': 5, 'name': 'Vegetarians United', 'impact': 8, 'info': 'Vegans and Non-Vegans co-exist.'},
#     { '_id': 6, 'name': 'I love my vegs', 'impact': 9, 'info': 'Save our planet one veggie at a time.'},
# ]

@app.route('/')
def users_index():
  #Show All users (and their total donations)
  return render_template('users_index.html', users=users.find(), donations=donations, charities=charities)

@app.route('/users/new')
def users_new():
  return render_template('users_new.html')

@app.route('/users', methods=['POST'])
def users_submit():
    """Submit a new user."""
    user = {
        'username': request.form.get('username'),
        'name': request.form.get('name'),
    }
    users.insert_one(user)
    return redirect(url_for('users_index'))


# turn the server on for serving... servering!
if __name__ == '__main__':
  app.run(debug=True, port=3000)

                 