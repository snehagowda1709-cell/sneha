from flask import Flask, request

app = Flask(_name_)

# Dummy sensitive info (for vulnerability demo)
DUMMY_USERNAME = "admin"
DUMMY_PASSWORD = "password123"
DUMMY_API_KEY = "12345-ABCDE-SECRET"
DUMMY_IP = "192.168.1.10"

@app.route("/")
def home():
    return """
    <h2>Welcome to Flask Security Demo</h2>
    <p><a href='/login'>Login Page</a></p>
    <p><a href='/secrets'>Sensitive Info (Vulnerable)</a></p>
    """

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        if username == DUMMY_USERNAME and password == DUMMY_PASSWORD:
            return f"<h3>Welcome, {username}!</h3><p>Go 
