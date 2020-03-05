
from wtforms import Form, StringField, TextAreaField, PasswordField, validators

class RegisterForm(Form):
    name = StringField('Name',[validators.length(min=2,max=50)])
    username = StringField('UserName', [validators.length(min=4, max=25)])
    email = StringField('Email', [validators.length(min=6, max=50)])
    password= PasswordField('Password',[
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Passwords do not match')
    ])
    confirm = PasswordField('Confirm Password')