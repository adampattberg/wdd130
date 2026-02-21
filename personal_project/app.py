from flask import Flask, render_template, request
import smtplib
import os
from email.mime.text import MIMEText

app = Flask(__name__)

# Home page
@app.route("/")
def home():
    return render_template("index.html")

# White Water Rafting page
@app.route("/white-water-rafting-webpage")
def white_water_rafting():
    return render_template("wwr.html")  # change to actual template if needed

# Site plan rafting page
@app.route("/site-plan-rafting")
def site_plan_rafting():
    return render_template("site-plan-rafting.html")

# ICE page
@app.route("/ice")
def ice():
    return render_template("ice.html")

# About page
@app.route("/about")
def about():
    return render_template("aboutme.html")

# Prophet Card
@app.route("/prophet-card")
def prophet_card():
    return render_template("ice/prophet_cards/nelson.html")

# Apostle Spotlights
@app.route("/apostle-spotlight")
def apostle_spotlight():
    return render_template("ice/apostle_spotlight/apostles.html")

# Favorite Devo
@app.route("/favorite-devo")
def favorite_devo():
    return render_template("ice/favorite_devo/favdevo.html")

# Valentines
@app.route("/valentines")
def valentines():
    return render_template("ice/valentines/index.html")

# Grid Flags
@app.route("/grid-flags")
def grid_flags():
    return render_template("ice/grid_flags/flags.html")

# Contact form submission
@app.route("/send", methods=["POST"])
def send():
    name = request.form.get("name")
    email = request.form.get("email")
    message = request.form.get("message")

    sender_email = os.environ.get("EMAIL_USER")
    sender_password = os.environ.get("EMAIL_PASS")
    receiver_email = "adam.pattberg@gmail.com"

    if not sender_email or not sender_password:
        print("ERROR: EMAIL_USER or EMAIL_PASS not set")
        return "Email configuration missing", 500

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

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, timeout=10) as server:
            server.login(sender_email, sender_password)
            server.send_message(msg)
    except Exception as e:
        print(f"Email sending failed: {e}")

    return render_template("thankyou.html")

# Only for local testing
if __name__ == "__main__":
    app.run(debug=True)