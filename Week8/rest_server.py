##basic flask server 
from flask import Flask, url_for, request, redirect, abort
app = Flask(__name__, static_url_path='', static_folder='staticpages')
books=[
{"id": 1, "Title": "Harry Potter", "Author": "JK", "Price": 1000},
{"id": 2, "Title": "some cook book", "Author": "Mr Angry Man", "Price": 2000},
{"id": 3, "Title": "Python made easy", "Author": "Some Liar", "Price": 1500}
]

#nextId=4

#app = Flask(__name__, static_url_path='', static_folder='staticpages')
@app.route('/')
def index():
    return "hello donal" 


@app.route('/books')
def getAll():
    #return books
    return "served by Get All()"

if __name__ == "__main__":
    app.run(debug=True) 