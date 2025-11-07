![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Flask](https://img.shields.io/badge/Flask-3.1-green)
![Render](https://img.shields.io/badge/Deployed%20on-Render-purple)


# 🗃️ Benard Joseph Tony - Portfolio Website

A fully functional **personal portfolio website** built with **Flask, HTML, CSS, and Bootstrap**,  showcasing my skills, services, and projects.  
It also includes a working **contact form** powered by **SendGrid**, allowing visitors to reach out securely and instantly.

[View Portfolio](https://benard-joseph-tony-portfolio.onrender.com)

---

## 🚀 Features

-  **Flask Backend** – lightweight and fast Python framework.
-  **Responsive UI** – built with HTML, CSS, and Bootstrap for seamless experience across all devices.
-  **Dynamic Portfolio Section** – project data loaded from a JSON file.
-  **Contact Form Integration** – SendGrid API used to send real-time messages.
-  **Environment Variables Support** – handled via `.env` file for security.
-  **Render Deployment** – fully deployed and live on Render.

---

## 🛠️ Tech Stack

| Category | Tools |
|-----------|--------|
| Backend Framework | Flask |
| Frontend | HTML, CSS, Bootstrap |
| Email Service | SendGrid API |
| Environment Management | python-dotenv |
| Deployment | Render |
| Language | Python 3 |

---

## 📁 Project Structure

```bash
portfolio-app/
├── .venv/                     # Virtual environment
├── data/
│   └── projects.json          # Your dynamic portfolio data ✅
├── static/
│   ├── images/                # Media and images ✅
│   └── styles.css             #  main CSS ✅
├── templates/
│   ├── base.html              # Layout file ✅
│   ├── about.html
│   ├── contact.html
│   ├── data_analytics.html
│   ├── footer.html
│   ├── header.html
│   ├── index.html
│   ├── llm_engineering.html
│   ├── portfolio.html
│   ├── services.html
│   ├── web_scrap.html
│   └── web_dev.html           
├── .env                       # Environment variables  ✅
├── .gitignore                 
├── main.py                    # main Flask app ✅
├── requirements.txt            # All dependencies ✅
└── Procfile                   # For Render deployment ✅
```



