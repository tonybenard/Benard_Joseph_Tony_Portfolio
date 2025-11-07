from flask import Flask, render_template, request, redirect, url_for, flash
from email.message import EmailMessage
from dotenv import load_dotenv
from datetime import datetime
from threading import Thread
import smtplib
import json
import os

load_dotenv()
app = Flask(__name__)
app.secret_key = os.getenv("KEY")  


EMAIL_ADDRESS = os.getenv("EMAIL_USER")
EMAIL_PASSWORD = os.getenv("EMAIL_PASS")
EMAIL_SERVER = os.getenv("MAIL_SERVER")
MAIL_FROM = os.getenv("MAIL_FROM")
MAIL_TO = os.getenv("MAIL_TO")
EMAIL_PORT = 465


# Async email sending function
def send_async_email(app, msg):
    """Send email in background thread to avoid blocking the request"""
    with app.app_context():
        try:
            with smtplib.SMTP_SSL(EMAIL_SERVER, EMAIL_PORT, timeout=30) as smtp:
                smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
                smtp.send_message(msg)
                print("Email sent successfully")
        except Exception as e:
            print(f"Email sending failed: {e}")


#Display current date across all pages
@app.context_processor
def inject_current_year():
    return {'current_year': datetime.now().year}

#home page
@app.route('/')
def home():
    return render_template('index.html')

#about page
@app.route('/about')
def about():
    return render_template('about.html')


#services page
@app.route('/services')
def services():
    return render_template("services.html")

@app.route('/services/web-development')
def web_dev():
    return render_template('web_dev.html')

@app.route('/services/web-scrap')
def web_scrap():
    return render_template('web_scrap.html')

@app.route('/services/data_analytics')
def data_analytics():
    return render_template('data_analytics.html')

@app.route('/services/llm_engineering')
def llm_engineering():
    return render_template('llm_engineering.html')


#portfolio page
@app.route('/portfolio')
def portfolio():
    with open('data/projects.json', 'r') as file:
        projects = json.load(file)
    return render_template('portfolio.html', projects=projects)


#Contact page
@app.route('/contact', methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        subject = request.form["subject"]
        message = request.form["message"]

        try:
            msg = EmailMessage()
            msg["From"] = MAIL_FROM
            msg["To"] = MAIL_TO
            msg["Subject"] = f"New Message from {name}: {subject}"
            msg.set_content(f"From: {name}\nEmail: {email}\n\nMessage:\n{message}")

            # Send email in background thread to avoid timeout
            Thread(target=send_async_email, args=(app, msg)).start()

            flash("Message sent successfully! ✅", "success")
            return redirect(url_for("contact"))

        except Exception as e:
            flash(f"Error: {str(e)}", "danger")
            return redirect(url_for("contact"))

    return render_template('contact.html')


if __name__ == "__main__":
    app.run(debug=True)