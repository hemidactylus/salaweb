'''
    forms.py : forms for userspace interactions
'''

from flask_wtf import FlaskForm
from wtforms import (
    StringField,
    BooleanField,
    SubmitField,
    HiddenField,
    PasswordField,
    TextAreaField,
    FormField,
    FieldList,
    Form,
)
from wtforms.validators import (
    InputRequired,
)

class LoginForm(FlaskForm):
    username = StringField('UserName', validators=[InputRequired()])
    password = PasswordField('Password', validators=[InputRequired()])
    login = SubmitField('Log In')
