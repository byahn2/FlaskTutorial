#Need to set environment variable "export FLASK_APP=flaskblog.py before running
#flask run
#can run in debug mode by setting export FLASK_DEBUG=1 or 

# render_template allows you to use templates and external html files
# url_for allows you to get the url for different functions and files
# flash allows you to send quick messages
# redirect sends users to a different route
from flask import Flask, render_template, url_for, flash, redirect

#import forms from the file you created called forms to insert them into templates
from forms import RegistrationForm, LoginForm

#create app variable and set to an instance of flask class
#__name__ is a special variable in python that is just the name of the model
app = Flask(__name__)


# Need a secret key for application which will protect against modifying cookies and other things
# python --> import secrets --> secrets.token_hex(16)
app.config['SECRET_KEY']='37bf29d14eb85a63c2db30a9e7b10e46'

#data to be used for the website
post_data = [
            {
                'author': 'Bryce Yahn',
                'title': 'Blog Post 1',
                'content': "It's teethpaste and you know it",
                'date_posted': 'April 20, 2018'
            },
            {
                'author': 'Sam King',
                'title': 'Blog Post 2',
                'content': 'pizza',
                'date_posted': 'September 20, 2018'
            }
        ]



#routes are what you type into the browser to go to different pages
#decorators are a way to add additional functionality to existing functions (handles backend stuff)

#"/" is the root page of website
#can have multiple routes
@app.route("/")
@app.route("/home")
# function returns information of page
# can pass data into functions.  will have access to the argument in our template
def home():
    return render_template('home.html', posts=post_data)

@app.route("/about")
def about():
    return render_template('about.html', title="About")


#Need to add a list of allowed method to recieve form
@app.route("/register", methods=['GET', 'POST'])
def register():
    # create an instance of a form to pass to the template
    form = RegistrationForm()
    #check if form validates when submitted
    if form.validate_on_submit():
        #use flash message to send a one time alert (first arg is message, second is category which is bootstrap class)
        flash(f'Acount created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title="Register", form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    # create an instance of a form to pass to the template
    form = LoginForm()
    #check if form validates when submitted
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == "password":
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful, Please check username and password', 'danger')
    return render_template('login.html', title="Login", form=form)


# double underscore name is main if we run the script with python directly (python flaskblog.py)
if __name__ == "__main__":
    app.run(debug=True)
