from flask import Flask, render_template, request, flash
from forms import ContactForm
from flask_mail import Mail, Message
from config import Config
from graphql import GraphQL
from pythonanywhere import PythonAnywhere
import git
import hmac
import hashlib

app = Flask(__name__)
Config.get_config()
app.config.from_object(Config)
mail = Mail(app)

def verify_signature(request):
    key = bytes(app.config['WEBHOOK_SECRET'], 'utf-8')
    expected_signature = hmac.new(key=key, msg=request.data, digestmod=hashlib.sha1).hexdigest()
    incoming_signature = request.headers.get('X-Hub-Signature').split('sha1=')[-1].strip()
    if not hmac.compare_digest(incoming_signature, expected_signature):
        return False
    return True

@app.route("/update", methods=['POST'])
def webhook():
        if request.method == 'POST':
            if verify_signature(request):
                repo = git.Repo('~/my_website')
                origin = repo.remotes.origin
                origin.pull()
                return 'Successfully updated.', 200
            return 'Forbidden', 403
        return 'Bad Request', 400

@app.route("/")
@app.route("/index")
def index():
    return render_template('index.html')

@app.route("/about")
def about():
    return render_template('about.html', title="About")
    
@app.route("/skills")
def skills():
    github_query = '''{ user(login: "joshguarino") {pinnedItems(first: 6, types: REPOSITORY) {
                            nodes {
                                ... on Repository {
                                    name
                                    url
                                    description
                                    }
                                }
                            }
                        }
                    }'''
    github = GraphQL(token=app.config['GITHUB_TOKEN'], url=app.config['GITHUB_URL'])
    data = github.post(github_query)
    repos = data['data']['user']['pinnedItems']['nodes']
    repo1 = repos[0:3]
    repo2 = repos[3:6]
    return render_template('skills.html', title="Skills", repos=[repo1, repo2])

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
        return render_template('submit.html', title="Contact", msg=f"Thank you {form.name.data} for your message.  I will get back to you as soon as possible.")
    elif request.method == 'GET':
        return render_template('contact.html', title="Contact", form=form)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('error.html', title="Error", the_error="404 Not Found", message="Sorry! The page you requested doesn't exist!"), 404

@app.errorhandler(405)
def page_not_found(e):
    return render_template('error.html', title="Error", the_error="405 Method Not Allowed", message="Sorry! Your not allowed to do that!"), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('error.html', title="Error", the_error="500 Internal Server Error", message="Sorry! My website is experiencing difficulties..."), 500

if __name__ == '__main__':
    app.run()