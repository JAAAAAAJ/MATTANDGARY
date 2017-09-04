from flask import *
from flask import Flask
SECRET_KEY = 'UNSW SURVEY SYSTEM COMP1531 S2 17'
app = Flask(__name__)
app.static_folder = 'static'
from file import write, read
# pulls in configurations by looking for UPPERCASE variables
app.config.from_object(__name__)

# Handle admin login
@app.route("/login", methods = ['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        # Check for correct login credentials
        if request.form['username'] == 'admin' or request.form['password'] == 'admin':
            session['logged_in'] = True
            return redirect(url_for('dashboard'))
        else:
            error = "Wrong username or password"

    return render_template("login.html", error=error)

@app.route("/dashboard", methods=['GET', 'POST'])
def dashboard():
    if request.method == "POST":
        question = request.form["question"]

        write([question])
    return render_template("dashboard.html")
