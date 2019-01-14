from flask import Flask, render_template
app = Flask(__name__)


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

@app.route("/contact")
def contact():
    return render_template('contact.html', title="Contact")

@app.errorhandler(404)
def page_not_found(e):
    return render_template('error.html', the_error="404 Not Found", message="Sorry! The page you requested doesn't exist!"), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('error.html', the_error="500 Internal Server Error", message="Sorry! My website is experiencing diffculties..."), 500



if __name__ == '__main__':
    app.run(debug=True, threaded=True)

