import flask
import os
from flask import request, redirect, render_template
from model import Database

app = flask.Flask("appName",static_url_path='/static')

@app.route('/', methods=['GET', 'POST'])
def index(): 
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    db = Database()
    
    if request.method == 'GET':
        return render_template('reg.html')
    
    if request.method == 'POST':
        username = request.form.get("username")
        email = request.form.get("email")
        password = request.form.get("psw")
        password_repeat = request.form.get("psw-repeat")

        if password == password_repeat and password_repeat != "" and password != "":
            db.insertUser(username, email, password)
            return redirect("/login")
        return render_template('reg.html')
    
@app.route('/login', methods=['GET', 'POST'])
def login():
    db = Database()
    if request.method == 'POST':
        username = request.form.get("username")
        password = request.form.get("password")
        if db.isUserValid(username, password):
            print("im okay")
            return redirect("/page2")
        else: 
            return redirect("/")
            
    if request.method == 'GET':
        return render_template('index.html')

@app.route('/page2', methods=['GET', 'POST'])
def second():
    if request.method == 'POST':
        return redirect('/')
    else:
        return render_template('page2.html')

@app.route('/book')
def getBook():
    return render_template('book.html', book=request.args.get('book'))

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host= '0.0.0.0', port= port, debug =True)
