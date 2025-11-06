from flask import Flask, render_template, request, redirect, url_for, flash
from email.message import EmailMessage
import smtplib
import json
import os
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()
app = Flask(__name__)
app.secret_key = os.getenv("KEY")  


EMAIL_ADDRESS = os.getenv("EMAIL_USER")
EMAIL_PASSWORD = os.getenv("EMAIL_PASS")


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
        sender_email = request.form["email"]
        subject = request.form["subject"]
        message_body = request.form["message"]

        msg = EmailMessage()
        msg["From"] = EMAIL_ADDRESS
        msg["To"] = EMAIL_ADDRESS 
        msg["Subject"] = f"Portfolio Contact: {subject}"
        msg.set_content(
            f"Name: {name}\nEmail: {sender_email}\n\nMessage:\n{message_body}"
        )

        try:
            with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
                smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
                smtp.send_message(msg)

            flash("✅ Your message has been sent successfully!", "success")
            return redirect(url_for("contact"))
        except Exception as e:
            print(e)
            flash("❌ Failed to send your message. Please try again.", "danger")
            return redirect(url_for("contact"))

    return render_template('contact.html')


if __name__ == "__main__":
    app.run()
