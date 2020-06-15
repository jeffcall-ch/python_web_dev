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

@app.route("/test/<search_query>")
def search(search_query):
    return search_query

@app.route("/integer/<int:value>")
def int_type(value):
    print (value + 1)
    return "correct"

@app.route("/name/<name>")
def index(name):
    if name.lower() == "michael":
        # return "Hello, {}".format(name), 200
        return f"Hello, {name}", 200
    else:
        return "Not found", 404

#start the dev server
if __name__ == "main":
    app.run()
