from flask import Flask, render_template, url_for, redirect, flash
import feedparser
import click
from models import create_tables, drop_tables, User
from flask_login import LoginManager, login_user, login_required, logout_user
from werkzeug.security import generate_password_hash, check_password_hash
from forms import LoginForm, RegisterForm

app = Flask(__name__)

app.secret_key = '5e8a85E7RED2^R'

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"


@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)


@app.route('/')
@login_required
def home():
    """Route vers la page d'accueil"""
    return render_template("index.html")


@app.route('/register', methods=['POST', 'GET'])
def register():
    """Route vers la page d'inscription"""
    form = RegisterForm()
    if form.validate_on_submit():
        user = User(
            username=form.username.data,
            password=generate_password_hash(form.password.data)
        )
        user.save()
        flash('Inscription réussi!')
        return redirect(url_for('login'))
    return render_template("register.html", form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    """Route vers la page de connexion"""
    form = LoginForm()

    if form.validate_on_submit():
        user = User.get(username=form.username.data)
        if user and check_password_hash(user.password, form.password.data):
            login_user(user)
            flash('Bienvenue')
            return redirect(url_for('home'))

    return render_template("login.html", form=form)


@login_required
@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route('/user/<username>')
@login_required
def user(username):
    """Route vers la page de l'utilisateur connecté"""
    return


@app.route('/list')
@login_required
def list():
    """Route vers la liste des utilisateurs inscrits sur le site"""
    return 

@app.cli.command()
def initdb():
    create_tables()
    click.echo("Database initialized !")


@app.cli.command()
def dropdb():
    drop_tables()
    click.echo("Database dropped !")
