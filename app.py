# flask imports
from flask import Flask, redirect, url_for, request, render_template, jsonify

# instantiate Flask object
app = Flask(__name__)

# Create some test data for our catalog in the form of a list of dictionaries.
books = [
    {
        "id": 1,
        "title":"Eloquent JavaScript, Third Edition",
        "subtitle":"A Modern Introduction to Programming",
        "author":"Marijn Haverbeke",
        "pages":472
    },
    {
        "id": 2,
        "title":"Practical Modern JavaScript",
        "subtitle":"Dive into ES6 and the Future of JavaScript",
        "author":"Nicolás Bevacqua",
        "pages":334
    },
    {
        "id": 3,
        "title":"Understanding ECMAScript 6",
        "subtitle":"The Definitive Guide for JavaScript Developers",
        "author":"Nicholas C. Zakas",
        "pages":352
    },
    {
        "id": 4,
        "title":"Speaking JavaScript",
        "subtitle":"An In-Depth Guide for Programmers",
        "author":"Axel Rauschmayer",
        "pages":460
    },
    {
        "id": 5,
        "title":"Learning JavaScript Design Patterns",
        "subtitle":"A JavaScript and jQuery Developer's Guide",
        "author":"Addy Osmani",
        "pages":254
    },
    {
        "id": 6,
        "title":"You Don't Know JS Yet",
        "subtitle":"Get Started",
        "author":"Kyle Simpson",
        "pages":143
    },
    {
        "id": 7,
        "title":"Pro Git",
        "subtitle":"Everything you neeed to know about Git",
        "author":"Scott Chacon and Ben Straub",
        "pages":458
    },
    {
        "id": 8,
        "title":"Rethinking Productivity in Software Engineering",
        "subtitle":"",
        "author":"Caitlin Sadowski, Thomas Zimmermann",
        "pages":310
    }
]

#quick test
# @app.route("/")
# def hello_world():
#     return "<p>Hello world!</p>"

# simple CRUD operations for the sample books that are defined above
@app.route("/", methods=['GET'])
def home():
    return '''<h1>Dan's Test Library</h2>
              <p>A Flask API for book information</p>
    '''

@app.route('/api/v1/books/all', methods=['GET'])
def api_all():
    return jsonify(books)

@app.route('/api/v1/books', methods=['GET'])
def api_id():
    if 'id' in request.args:
        id=int(request.args['id'])
    else:
        return "Error: No id field provided."

    results = []
    for book in books:
        if book['id'] == id:
            results.append(book)

    return jsonify(results)

@app.route('/api/v1/books', methods=['POST'])
def api_insert():
    book = request.get_json()
    books.append(book)
    return "Success: book info has been added."

@app.route('/api/v1/books/<id>', methods=['DELETE'])
def api_delete(id):
    for book in books:
        if book['id'] == int(id):
            books.remove(book)
        
    return "Success: book has been removed."

# the first stuff that I was working on
@app.route('/check/<name>')
def check(name):
    return f'Welcome to my Flask Test Project, {name}! Go to api/v1/books to get started.'

@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        user = request.form['sampname']
        return redirect(url_for('check', name=user))
    else:
        return "ERROR: INVALID REQUEST"

if __name__ == '__main__':
    app.run(debug=True)