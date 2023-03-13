from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class Lf(FlaskForm):
    name = StringField("Name: ", validators=[DataRequired()])
    email = StringField("eMail: ", validators=[DataRequired()])
    password = StringField("Password: ", validators=[DataRequired()])
    password_again = StringField("Password again: ", validators=[DataRequired()])
    remember_me = BooleanField("Remember? ")
    submit = SubmitField("Registration")

