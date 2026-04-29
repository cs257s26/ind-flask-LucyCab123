from flask import Flask
import csv
from ProductionCode.command_line import *

app = Flask(__name__)

Interface = Search()


@app.route('/')
def homepage():
    return ("Hello! To use this website, add '/' followed by 'name/<name>' or 'type/<type>' to the URL!")

@app.route('/type/<string:animal>/')
def getType(animal):
    listOfType = Interface.typeToList(animal)
    if listOfType == []:
        return "Sorry! No info found; make sure you entered a valid classification!"
    return listOfType

@app.route('/name/<string:animal>/')
def getAnimal(animal):
    Name = Interface.nameToInfo(animal)
    if Name == []:
        return "Sorry! No animal found. Make sure you are entering the taxonomical name! Not all names are common names!"    
    return Name


@app.errorhandler(404)
def page_not_found(e):
     return "sorry, wrong format! Make sure your URL looks like 'http://127.0.0.1:<port>/'type/name'/'search criteria'"

@app.errorhandler(500)
def python_bug(e):
     return "Uh oh! Looks like something is wrong on our end. Sorry about that!"

if __name__ == '__main__':
    app.run(port=5100)