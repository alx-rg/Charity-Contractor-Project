
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

from flask import Flask, render_template
from pymongo import MongoClient
from flask import Flask, render_template, request, redirect, url_for
from  bson.objectid import ObjectId

client = MongoClient()
db = client.Charity
charity = db.charities
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

/charities	        GET	        index	    See all charities
/charities/new	    GET	        new	      See new charity form
/charities	        POST	      create	  Create a new charity
/charities/:id	    GET	        show	    See one charity
/charities/:id/edit	GET	        edit	    See an edit charity form
/charities/:id	    PATCH/PUT	  update	  Update a charity
/charities/:id	    DELETE	    destroy	  Delete a charity

/donations	        GET	        index	    See all donations
/donations/new	    GET	        new	      See new donation form
/donations	        POST	      create	  Create a new donation
/donations/:id	    GET	        show	    See one donation
/donations/:id/edit	GET	        edit	    See an edit donation form
/donations/:id	    PATCH/PUT	  update	  Update a donation
/donations/:id	    DELETE	    destroy	  Delete a donation

 """


# users = [
#     { 'name': 'Jim Corning', 'charity': 'Humane Society', 'donation': 1000 },
#     { 'name': 'George Lucas', 'charity': 'Dogs For Life', 'donation': 250 }
# ]

# charities = [
#     { 'name': 'Humane Society', 'impact': 10, 'report': 'Helps dogs find new homes, succesful 100%.', '_id': 1}, 
#     { 'name': 'Dogs For Life', 'impact': 9, 'report': 'Dogs and wonderful families.', '_id': 2},
#     { 'name': 'MooseDoodle Shelter', 'impact': 10, 'report': 'Shelter 4 dogs.', '_id': 3},
#     { 'name': 'Green Peace Dogs', 'impact': 8, 'report': 'Saves dogs in the food trade.', '_id': 4},
#     { 'name': 'Vegetarians United', 'impact': 8, 'report': 'Vegans and Non-Vegans co-exist.', '_id': 5},
#     { 'name': 'I love my vegs', 'impact': 9, 'report': 'Save our planet one veggie at a time.', '_id': 6},
# ]

@app.route('/')
def users_index():
  #Show All users (and their total donations)
  return render_template('users_index.html', users=users.find())

# turn the server on for serving... servering!
if __name__ == '__main__':
  app.run(debug=True, port=3000)

                 