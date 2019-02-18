from flask import Flask, render_template, request
from forms import ContactForm
from config import Config

app = Flask(__name__)

app.config.from_object(Config)

@app.route("/")
@app.route("/index")
def index():
    return render_template('index.html')

@app.route("/about")
def about():
    return render_template('about.html', title="About")
    
@app.route("/skills")
def skills():
    return render_template('skills.html', title="Skills")

@app.route("/contact", methods=['GET','POST'])
def contact():
    form = ContactForm()
    if request.method == 'POST':
        return 'Form posted.'
    elif request.method == 'GET':
        return render_template('contact.html', title="Contact", form=form)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('error.html', the_error="404 Not Found", message="Sorry! The page you requested doesn't exist!"), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('error.html', the_error="500 Internal Server Error", message="Sorry! My website is experiencing diffculties..."), 500



if __name__ == '__main__':
    app.run()

