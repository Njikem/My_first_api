from flask import Flask
from dbhelpers import run_statement
import json

app = Flask(__name__)


@app.route("/animal")
def get_animals():
    result = run_statement("call get_all_animals()", [])
    if(type(result == list)):
        return result
    else:
        return "Sorry something went wrong. Try again." 


@app.route("/dog")
def get_dog():
    result = run_statement("call get_dog()", [])
    if(type(result == list)):
        return result
    else: 
        return "Sorry something went wrong. Try again. "


@app.route("/cat")
def get_cat():
    result = run_statement("call get_cat()", [])
    if(type(result == list)):
        return result
    else: 
        return "Sorry something went wrong. Try again."
       




app.run(debug=True)