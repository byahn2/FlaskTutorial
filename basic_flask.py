#Need to set environment variable "export FLASK_APP=flaskblog.py before running
#flask run
#can run in debug mode by setting export FLASK_DEBUG=1 or 

from flask import Flask
#create app variable and set to an instance of flask class
#__name__ is a special variable in python that is just the name of the model
app = Flask(__name__)

#routes are what you type into the browser to go to different pages
#decorators are a way to add additional functionality to existing functions (handles backend stuff)
#"/" is the root page of website
@app.route("/")
#can have multiple routes
@app.route("/home")
# function returns information of page
def hello():
    return "<h1>Home Page</h1>"

@app.route("/about")
def about():
    return "<h1>About World!</h1>"



# double underscore name is main if we run the script with python directly (python flaskblog.py)
if __name__ == "__main__":
    app.run(debug=True)
