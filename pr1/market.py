from flask import Flask, render_template
import secrets
app = Flask(__name__)


@app.route("/")
@app.route("/home") #they will both lead to the same page 
def home_page():
    return render_template('home.html')

@app.route("/about/<username>") #dynamic stuff
def ungay(username): #The route name variable passes to the function and fills in the fstring
    return f"<h1>This is about the page of {username}"
app.config['SECRET_KEY'] = secrets.token_urlsafe(128)
if __name__ == "__main__":
    app.run(debug=True)