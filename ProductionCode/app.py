from flask import Flask
import csv
from ProductionCode.command_line import *

app = Flask(__name__)

Interface = Search()


@app.route('/')
def homepage():
    #String instructing user how to use the website
    return ("Hello! To use this website, add '/' followed by 'name/<name>' or 'type/<type>' to the URL!")

@app.route('/type/<string:type>/')
def getType(type):
    #Takes in input of type followed by whatever type they wish to search by
    listOfType = Interface.typeToList(type)
    if listOfType == []:
        #if listOfType is empty, no valid results were found. Return this error message to the user
        return "Sorry! No info found; make sure you entered a valid classification!"
    return listOfType

@app.route('/name/<string:animal>/')
def getAnimal(animal):
    #same as above route, but altered to be name/animal specific.
    Name = Interface.nameToInfo(animal)
    if Name == []:
        return "Sorry! No animal found. Make sure you are entering the taxonomical name! Not all names are common names!"    
    return Name


@app.errorhandler(404)
def page_not_found(e):
     return "sorry, wrong format! Make sure your URL looks like 'http://127.0.0.1:<port>/'type/name'/'search criteria"

@app.errorhandler(500)
def python_bug(e):
     return "Uh oh! Looks like something is wrong on our end. Sorry about that!"

if __name__ == '__main__':
    app.run(port=5100)