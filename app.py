from flask import Flask, render_template

app = Flask(__name__)

@app.route('/homepage')
def homePage():
    return render_template("index.html")

@app.route('/register')
def registerPage():
    return render_template("register.html")

@app.route('/signin')
def signInPage():
    return render_template("signin.html")

@app.route('/user/<username>')
def userPage(username):
    return 
