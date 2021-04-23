import time
from flask import Flask

app = Flask(__name__)

@app.route('/')
def give_array_of_data():
    return str([1,2,3,4,5])
    
@app.route('/hello')
def hello():
    return "hello world"

@app.route('/search_movie/<movie>')
def show_movie(movie):
    ret = ""
    for i in range(len(movie)):
        if movie[i] == "_":
            ret += " "
        else:
            ret += movie[i]
    return ret

@app.route("/rec_movies")
def rec_movies():
    list_item = [{'id':'1', 'title':'movie','genre':'horror'}]
    return str(list_item)