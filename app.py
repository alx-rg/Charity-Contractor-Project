
# env/bin/activate
# If you ever want to deactivate your virtual environment, just type deactivate in your terminal window.#
# export FLASK_ENV=development; flask run
# http://127.0.0.1:5000/
# localhost:5000

from flask import Flask, render_template

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

/donations	        GET	        index	    See all donations
/donations/new	    GET	        new	      See new donation form
/donations	        POST	      create	  Create a new donation
/donations/:id	    GET	        show	    See one donation
/donations/:id/edit	GET	        edit	    See an edit donation form
/donations/:id	    PATCH/PUT	  update	  Update a donation
/donations/:id	    DELETE	    destroy	  Delete a donation

/charities	        GET	        index	    See all charities
/charities/new	    GET	        new	      See new charity form
/charities	        POST	      create	  Create a new charity
/charities/:id	    GET	        show	    See one charity
/charities/:id/edit	GET	        edit	    See an edit charity form
/charities/:id	    PATCH/PUT	  update	  Update a charity
/charities/:id	    DELETE	    destroy	  Delete a charity
 """

users = [
    { 'name': 'Jim Corning', 'charity': 'Humane Society', 'donation': 1000 },
    { 'name': 'George Lucas', 'charity': 'Dogs For Life', 'donation': 250 }
]

@app.route('/')
def users_index():
  #Show All users (and their total donations)
  return render_template('users_index.html', users=users)

# turn the server on for serving... servering!
if __name__ == '__main__':
  app.run(debug=True, port=3000)

                 