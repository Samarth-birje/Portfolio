from flask import Flask, render_template

app = Flask(__name__, static_folder="static", template_folder="templates")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/projects")
def projects():
    return render_template("/projects.html")

@app.route("/contact")
def contact():
    return render_template("/contact.html")

@app.route("/base")
def base():
    return render_template("/base.html")


if __name__ == "__main__":
    app.run(debug=True)