#Flask hello world!
from flask import Flask

#create app object
app = Flask(__name__)

#use decorator to link to an url
@app.route("/")
@app.route("/hello")

#define the view using a function to return a string
def hello_world():
    return "Hello World!"

#start the dev server
if __name__ == "main":
    app.run()

#to get it run use terminal https://flask.palletsprojects.com/en/1.1.x/quickstart/
#$ export FLASK_APP=app.py
#$ flask run