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


if __name__ == '__main__':
    app.run(debug=True, threaded=True)

