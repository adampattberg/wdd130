from flask import Flask, render_template, request
import smtplib
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

    sender_email = "adam.pattberg@gmail.com"
    sender_password = "yceq jjih pcfo wxcd"   # Gmail app password
    receiver_email = "adam.pattberg#gmail.com"

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

    return "Message sent successfully!"

if __name__ == "__main__":
    app.run(debug=True)