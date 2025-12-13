from flask import Flask,render_template
app = Flask(__name__)

@app.route("/")
def homePage():
    return "<h1> Hello from your first App!<p>Ther server is running !</p>"

@app.route("/greet/<name>")
def greet_user(name):
    return f"<h2>Welcome,{name.capitalize()}h2>"

@app.route("/report/<username>/<int:score>")
def show_report(username, score):
    # Flask looks for 'report.html' inside the 'templates' folder
    return render_template(
        "report.html", 
        user=username, 
        current_score=score
    )

if __name__=="__main__":
    app.run(debug=True)
