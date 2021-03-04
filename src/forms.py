from flask_wtf  import FlaskForm, RecaptchaField, Recaptcha
from wtforms import TextField, TextAreaField, SubmitField, validators, ValidationError
 
class ContactForm(FlaskForm):
  name = TextField("Name", [validators.Required("Please enter your name.")])
  email = TextField("Email", [validators.Required("Please enter your email address."), validators.Email("Please enter your email address.")])
  subject = TextField("Subject", [validators.Required("Please enter a subject.")])
  message = TextAreaField("Message", [validators.Required("Please enter a message.")])
  recaptcha = RecaptchaField(validators=[Recaptcha(message="Please prove you're not a robot")])
  submit = SubmitField("Send")
 