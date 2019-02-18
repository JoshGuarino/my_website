from flask_wtf  import FlaskForm
from wtforms import TextField, TextAreaField, SubmitField
 
class ContactForm(FlaskForm):
  name = TextField("Name")
  email = TextField("Email")
  subject = TextField("Subject")
  message = TextAreaField("Message")
  submit = SubmitField("Send")