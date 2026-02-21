from flask import Flask, render_template, request
import smtplib
import os
from email.mime.text import MIMEText

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/send", methods=["POST"])
def send():
    name = request.form["name"]
    email = request.form["email"]
    message = request.form["message"]

    sender_email = os.environ.get("EMAIL_USER")
    sender_password = os.environ.get("EMAIL_PASS")
    receiver_email = "adam.pattberg@gmail.com"

    body = f"""
New Contact Form Submission

Name: {name}
Email: {email}
Message:
{message}
"""

    msg = MIMEText(body)
    msg["Subject"] = "Portfolio Contact Form"
    msg["From"] = sender_email
    msg["To"] = receiver_email

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(sender_email, sender_password)
        server.send_message(msg)

    return render_template("thankyou.html")

if __name__ == "__main__":
    app.run()

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("aboutme.html")

@app.route("/ice")
def ice():
    return render_template("ice.html")

@app.route("/site-plan-rafting")
def site_plan_rafting():
    return render_template("site-plan-rafting.html")