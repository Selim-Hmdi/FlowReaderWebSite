from flask import Flask, render_template, url_for, redirect, flash
import feedparser
import click
import os
from models import create_tables, drop_tables, User, create_user, Flow
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from forms import LoginForm, RegisterForm, URLForm

app = Flask(__name__)

app.secret_key = '5e8a85E7RED2^Raa7Z^ùr'

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"


@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)


@app.route('/')
def home():
    """Route vers la page d'accueil"""
    user_id = current_user.get_id()
    query = Flow.select(Flow.url,Flow.id).join(User).where(User.id == user_id)
    feedRSS = dict()
    feedAtom = dict()
    for flow in query:
        d = feedparser.parse(flow.url)
        if "rss" in d.version: #Flux rss
            feedRSS[flow.url] = d
        else: #Flux atom
            feedAtom[flow.url] = d
    return render_template("index.html", feedRSS=feedRSS, feedAtom=feedAtom)


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
        flash('Done')
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
            flash('Welcome')
            return redirect(url_for('home'))

    return render_template("login.html", form=form)

@login_required
@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))

@app.route('/flow', methods=['GET', 'POST'])
@login_required
def flow():
    """Route vers le lecteur d'URL pour flux rss/atom"""
    user_id = current_user.get_id()
    form = URLForm()
    if form.validate_on_submit():
        flow = Flow(
            url = form.url.data,
            user = user_id
        )
        flow.save()
        print ('User id : {0}\nUrl : {1}\nid du flow {2}'.format(flow.user,flow.url,flow.id))
    return render_template("flow.html", form=form)



@app.cli.command()
def initdb():
    create_tables()
    click.echo("Database initialized !")


@app.cli.command()
def dropdb():
    drop_tables()
    click.echo("Database dropped !")


@app.cli.command()
def createuser():
    create_user()
    click.echo("Users toto and thor created")
