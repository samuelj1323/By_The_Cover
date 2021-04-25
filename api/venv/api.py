import time
from flask import Flask, make_response

app = Flask(__name__)
import analysis
@app.route("/api/endpoint")
def endpoint():
    resp = make_response({"cat": 15})
    resp.headers["Access-Control-Allow-Origin"] = "*"
    return resp

@app.route('/')
def give_array_of_data():
    return str([1,2,3,4,5])
    
@app.route('/hello')
def hello():
    return "hello world"

@app.route('/search_movie/<movie>')
def show_movie(movie):
    ret = ""
    #for i in range(len(movie)):
    #    if movie[i] == "_":
    #        ret += " "
    #    else:
    #        ret += movie[i]
    return analysis.analyze(movie)
    #return ret

@app.route("/rec_movies")
def rec_movies():
    list_item = [{'id':'1', 'title':'movie','genre':'horror'}]
    return str(list_item)
    