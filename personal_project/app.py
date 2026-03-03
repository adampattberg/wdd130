from flask import Flask, render_template, request
import os
import resend

app = Flask(__name__)

# Set Resend API key
resend.api_key = os.environ.get("RESEND_API_KEY")

# ---------------- ROUTES ----------------

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/white-water-rafting-webpage")
def white_water_rafting():
    return render_template("wwr.html")

@app.route("/site-plan-rafting")
def site_plan_rafting():
    return render_template("site-plan-rafting.html")

@app.route("/ice")
def ice():
    return render_template("ice.html")

@app.route("/about")
def about():
    return render_template("aboutme.html")

@app.route("/prophet-card")
def prophet_card():
    return render_template("ice/prophet_cards/nelson.html")

@app.route("/apostle-spotlight")
def apostle_spotlight():
    return render_template("ice/apostle_spotlight/apostles.html")

@app.route("/favorite-devo")
def favorite_devo():
    return render_template("ice/favorite_devo/favdevo.html")

@app.route("/valentines")
def valentines():
    return render_template("ice/valentines/index.html")

@app.route("/grid-flags")
def grid_flags():
    return render_template("ice/grid_flags/flags.html")

@app.route("/positioning")
def positioning():
    return render_template("ice/positioning/positioning.html")

@app.route("/gallery")
def gallery():
    return render_template("ice/gallery/gallery.html")

@app.route("/signup")
def signup():
    return render_template("ice/signup/signup.html")

# ---------------- EMAIL ----------------

@app.route("/send", methods=["POST"])
def send():
    name = request.form.get("name")
    email = request.form.get("email")
    message_text = request.form.get("message")

    body = f"""
New Contact Form Submission

Name: {name}
Email: {email}

Message:
{message_text}
"""

    try:
        resend.Emails.send({
            "from": "Portfolio <onboarding@resend.dev>",  # works without domain setup
            "to": ["adam.pattberg@gmail.com"],
            "subject": "Portfolio Contact Form",
            "text": body,
        })
        print("Email sent successfully")

    except Exception as e:
        print("Resend error:", e)
        return "Failed to send email", 500

    return render_template("thankyou.html")

# ---------------- LOCAL RUN ----------------

if __name__ == "__main__":
    app.run(debug=True)