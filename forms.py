# put forms in their own files

#write python classes representative of forms that will automatically be converted to html
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
# validators used to cosntrain form inputs
from wtforms.validators import DataRequired, Length, Email, EqualTo

# this form inherits from FlaskForm
class RegistrationForm(FlaskForm):
    #create an attribute from a string field where the first argument is the name of the field
    #first argument also used as the label in our html
    # second argument is a list of validations we want to check
    username = StringField('Username', 
            validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', 
            validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign_Up')



class LoginForm(FlaskForm):
    #create an attribute from a string field where the first argument is the name of the field
    #first argument also used as the label in our html
    # second argument is a list of validations we want to check
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    #remember field uses a secure cookie
    remember = BooleanField('Remember Me')
    submit = SubmitField('LogIn')


