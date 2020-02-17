from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, PasswordField
from wtforms.fields.html5 import DateField
from wtforms.validators import DataRequired, Length, EqualTo


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[
                           DataRequired(), Length(min=3, max=18)])
    password = PasswordField("Password", validators=[DataRequired()])


class RegisterForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired(), Length(min=3, max=18)])
    password = PasswordField("Password", validators=[DataRequired(), 
                            EqualTo('confirmPassword', message="Les deux mot de passe doivent correspondre")])
    confirmPassword = PasswordField("Confirm password")


class URLForm(FlaskForm):
    url = StringField("Url du flux", validators=[DataRequired()])
