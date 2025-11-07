from flask import Flask, render_template, request, redirect, url_for, flash
from dotenv import load_dotenv
from datetime import datetime
from threading import Thread
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
import json
import os

# Load environment variables
load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv("KEY")

# SendGrid credentials
SENDGRID_API_KEY = os.getenv("SENDGRID_API_KEY")
MAIL_FROM = os.getenv("MAIL_FROM")
MAIL_TO = os.getenv("MAIL_TO")


# Async SendGrid email sender
def send_async_email(app, message):
    with app.app_context():
        try:
            sg = SendGridAPIClient(SENDGRID_API_KEY)
            response = sg.send(message)
            print(f"Email sent! Status code: {response.status_code}")
        except Exception as e:
            print(f"SendGrid email error: {e}")


# Display current year globally
@app.context_processor
def inject_current_year():
    return {'current_year': datetime.now().year}


# Routes
# Home Page
@app.route('/')
def home():
    return render_template('index.html')

# About Page
@app.route('/about')
def about():
    return render_template('about.html')

# Services Page
@app.route('/services')
def services():
    return render_template("services.html")

@app.route('/services/web_dev')
def web_dev():
    return render_template('web_dev.html')

@app.route('/services/data_analytics')
def data_analytics():
    return render_template('data_analytics.html')

@app.route('/services/llm_engineering')
def llm_engineering():
    return render_template('llm_engineering.html')

@app.route('/services/web_scrap')
def web_scrap():
    return render_template('web_scrap.html')


@app.route('/portfolio')
def portfolio():
    with open('data/projects.json', 'r') as file:
        projects = json.load(file)
    return render_template('portfolio.html', projects=projects)


@app.route('/contact', methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        subject = request.form["subject"]
        message_body = request.form["message"]

        try:
            message = Mail(
                from_email=MAIL_FROM,
                to_emails=MAIL_TO,
                subject=f"New Message from {name}: {subject}",
                plain_text_content=f"From: {name}\nEmail: {email}\n\nMessage:\n{message_body}"
            )

            Thread(target=send_async_email, args=(app, message)).start()

            flash("Message sent successfully! ✅", "success")
            return redirect(url_for("contact"))

        except Exception as e:
            flash(f"Error: {str(e)}", "danger")
            return redirect(url_for("contact"))

    return render_template('contact.html')


if __name__ == "__main__":
    app.run()
