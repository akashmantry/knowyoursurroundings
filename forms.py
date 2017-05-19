from flask_wtf import Form
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length

class SignupForm(Form):
	first_name = StringField("First name", validators = [DataRequired("Firstname required!")])
	last_name = StringField("Last name", validators = [DataRequired("Lastname required!")])
	email = StringField("Email", validators = [DataRequired("Email required!"), Email("Enter valid email!")])
	password = PasswordField("Password", validators = [DataRequired("Password required!"), Length(min=6, message="Password must be atleast 6 characters long!")])
	submit = SubmitField("Sign Up")

class LoginForm(Form):
	email = StringField("Email", validators = [DataRequired("Email required!"), Email("Enter valid email!")])
	password = PasswordField("Password", validators = [DataRequired("Password required!"), Length(min=6, message="Password must be atleast 6 characters long!")])
	submit = SubmitField("Sign In")

class AddressForm(Form):
	address = StringField("Address", validators = [DataRequired("Address required!")])
	submit = SubmitField("Search")