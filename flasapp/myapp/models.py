
from wtforms import Form, StringField, TextAreaField, PasswordField, validators
from wtforms.validators import DataRequired, Length, Email, EqualTo

class RegisterForm(Form):
    name = StringField('Name',[validators.length(min=2,max=50)])
    username = StringField('UserName', [validators.length(min=4, max=25)])
    email = StringField('Email', validators=[DataRequired(),Email()])
    password = PasswordField('Password(Min Length 8)', validators=[DataRequired(), Length(min=8)])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])