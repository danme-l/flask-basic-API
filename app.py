# flask imports
from flask import Flask, redirect, url_for, request, render_template

# instantiate Flask object
app = Flask(__name__)

#quick test
@app.route("/")
def hello_world():
    return "<p>Hello world!</p>"

# route() decorator tells Flask which URL to trigger the function
@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)


@app.route('/check/<name>')
def check(name):
    retString = 'Welcome to my Flask Test Project, %s!' %name
    return retString

@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        user = request.form['danmeleras']
        return redirect(url_for('check', name=user))
    else:
        return "ERROR: INVALID REQUEST"

if __name__ == '__main__':
    app.run(debug=True)