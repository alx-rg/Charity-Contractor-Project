
# python3 -m venv env
# source env/bin/activate 
# If you ever want to deactivate your virtual environment, just type deactivate in your terminal window.#
# export FLASK_ENV=development; flask run
# http://127.0.0.1:5000/
# localhost:5000

# MongoDB     brew services start mongodb-community@5.0     Verify that it's running with : brew services list
# to stop MongoDB brew services stop mongodb-community@5.0

from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient
from bson.objectid import ObjectId
import os

uri = os.environ.get('MONGODB_URI')
client = MongoClient(uri)
db = client.get_database('CharityTracker')

app = Flask(__name__)

""" 
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
  #Show All users
  users = db.users.find({})
  return render_template('users_index.html', users=users)
  # , donations=donations, charities=charities)

@app.route('/users/new')
def users_new():
  user = {
    'username': "",
    'name': "",
  }
  return render_template('users_new.html', user=user, title='New User')

@app.route('/users', methods=['POST'])
def users_submit():
    """Submit a new user."""
    user = {
        'username': request.form.get('username'),
        'name': request.form.get('name'),
    }
    db.users.insert_one(user)
    return redirect(url_for('users_index'))

@app.route('/users/<user_id>')
def users_show(user_id):
  user = db.users.find_one({'_id': ObjectId(user_id)})
  #users_donations = donations.find({'users_id': users_id}
  return render_template('users_show.html', user=user) 
  #, donations=users_donations)

@app.route('/users/<user_id>/edit')
def users_edit(user_id):
  user = db.users.find_one({'_id': ObjectId(user_id)})
  return render_template('users_edit.html', user=user, title='Edit User')

@app.route('/users/<user_id>', methods=['POST'])
def users_update(user_id):
    updated_user = {
        'username': request.form.get('username'),
        'name': request.form.get('name'),
    }
    db.users.update_one(
        {'_id': ObjectId(user_id)},
        {'$set': updated_user})
    return redirect(url_for('users_show', user_id=user_id))

@app.route('/users/<user_id>/delete', methods=['POST'])
def users_del(user_id):
    db.users.delete_one({'_id': ObjectId(user_id)})
    return redirect(url_for('users_index'))


# NEW DONATION BELOW: --------------------------------------------------------------

@app.route('/donations/new')
def donation_new():
  # Hidden Form element to add the donation to the user
    return render_template('donations_new.html')

"""
@app.route('users/donations', method=['POST'])
def donations_new():
  donation = {
      'user_id': request.form.get('user_id'),
    # Name of the charity
      'charityName': request.form.get('charity'),
    # Calendar Picker for Date of Donation
      'date': request.form.get('date'),
    # Amount of Donation
      'amount': request.form.get('amount'),
    }
  db.donations.insert_one(donation)
  return redirect(url_for('users_show', user_id=user_id))
  # Hidden Form element to add the donation to the user
"""

@app.route('/donations', methods=['POST'])
def donation_submit():
    db.donation = {
      #Drop Down list of Users
        'username': request.form.get('username'),
      # Drop Down Name Of Charity
        'name': request.form.get('charity'),
      # Calendar Picker for Date of Donation
        'date': request.form.get('date'),
      # Amount of Donation
        'amount': request.form.get('amount'),
      }
    db.donations.insert_one(donation)
    return redirect(url_for('donations_index'))

@app.route('/donations/<donations_id>/remove', methods=['POST'])
def donations_del(donations_id):
    db.donations.delete_one({'_id': ObjectId(donations_id)})
    return redirect(url_for('donations_index'))

#DONATION ABOVE: --------------------------------------------------------------    

#CHARITIES BELOW: --------------------------------------------------------------    

@app.route('/charities/new')
def charities_new():
    return render_template('charities_new.html')

#CHARITIES ABOVE: --------------------------------------------------------------    



# turn the server on for serving... servering!
if __name__ == '__main__':
  app.run(debug=True, port=3000)

                 