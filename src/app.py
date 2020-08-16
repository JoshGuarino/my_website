from flask import Flask, render_template, request, flash
from forms import ContactForm
from flask_mail import Mail, Message
from config import Config
from graphql import GraphQL

app = Flask(__name__)
Config.get_config()
app.config.from_object(Config)
mail = Mail(app)

@app.route("/")
@app.route("/index")
def index():
    return render_template('index.html')

@app.route("/about")
def about():
    return render_template('about.html', title="About")
    
@app.route("/skills")
def skills():
    github = GraphQL(token=app.config['GITHUB_TOKEN'], url=app.config['GITHUB_URL'])
    data = github.post(app.config['GITHUB_QUERY'])
    return render_template('skills.html', title="Skills", repos=data)

@app.route("/contact", methods=['GET','POST'])
def contact():
    form = ContactForm()
    if request.method == 'POST':
        if form.validate() == False:
            flash('All fields are required.')
            return render_template('contact.html', form=form, title="Contact")
        msg = Message(form.subject.data, sender=app.config['MAIL_USERNAME'], recipients=[app.config['MAIL_RECIEVE']])
        msg.body = """
        From: %s <%s>
        %s
        """ % (form.name.data, form.email.data, form.message.data)
        mail.send(msg)
        return render_template('submit.html', title="Contact", msg="Thank you " + form.name.data + " for your message.  I will get back to you as soon as possible.")
    elif request.method == 'GET':
        return render_template('contact.html', title="Contact", form=form)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('error.html', the_error="404 Not Found", message="Sorry! The page you requested doesn't exist!"), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('error.html', the_error="500 Internal Server Error", message="Sorry! My website is experiencing difficulties..."), 500

if __name__ == '__main__':
    app.run()

