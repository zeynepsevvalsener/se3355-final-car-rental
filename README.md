# 🚗 SE3355 Final Car Rental

## 🏁 Introduction  
**SE3355 Final Car Rental** is a modern web application that simplifies car rental services. Users can browse available cars, make reservations, and complete transactions seamlessly.

📢 **Objective**  
The goal of this project is to digitize the **car rental process**, making it more efficient and user-friendly.

---
se3355-final-car-rental/
│── /vehicles               # Ana Django Uygulaması
│── /MyApp                  # İş mantığı ve modeller
│── /static                 # CSS, JS ve medya dosyaları
│── /templates              # HTML şablonları
│── .env                    # Gizli anahtarlar (Git'e eklenmez)
│── manage.py               # Django Yönetim Komutları
│── README.md               # Dokümantasyon

---

## ✨ Features  

✅ **Browse & Filter Cars**  
✅ **Find the Nearest Office on a Map**  
✅ **Google OAuth Login & Authentication**  
✅ **Booking & Rental Management**  
✅ **User Dashboard**  

---
## About Django : 
Django is an MVT (Model-View-Template) web framework designed for building robust and scalable web applications. It comes with a built-in administration interface, allowing developers to manage models, user permissions, and user groups effortlessly. With this integrated admin panel, there is often no need for an external database management tool, except for handling advanced database operations.
Django also provides secure password handling, verifying user credentials by hashing the entered password and comparing it to the stored hash value. Internally, Django offers multiple built-in options for various functionalities, such as database backends and templating engines. However, it is also highly extensible, allowing developers to integrate third-party components when needed.

---  

### 🚀 Backend (Server-Side)
- **Django** - High-level Python web framework that promotes rapid development and clean, pragmatic design.
- **Django REST Framework (DRF)** - Used for building APIs and handling serialization.
- **SQLite** - Lightweight database for local development; can be replaced with PostgreSQL or MySQL in production.
- **Django-Allauth** - Provides built-in authentication and third-party login support (Google OAuth).

### 🎨 Frontend (Client-Side)
- **Django Templates** - Server-side rendering of HTML pages.
- **Bootstrap** - A responsive CSS framework for a mobile-friendly UI.
- **JavaScript (Vanilla JS & jQuery)** - Enhancing user interactions and AJAX calls.

### 💾 Database
- **SQLite** - Default database for development.

### 🔑 Authentication & Security
- **Google OAuth (Django-Allauth)** - Enables social authentication with Google.
- **Django's Built-in Authentication System** - Handles user authentication securely.
- **Django-Hardened Security Features** - CSRF protection, XSS protection, and password hashing.

### 📡 API & Data Handling
- **Django REST Framework** - Used for creating and managing RESTful APIs.
- **JSON Web Tokens (JWT)**  - For secure API authentication.

### 📦 Package & Dependency Management
- **pip** - Python package manager to install dependencies.
- **python-dotenv** - Loads environment variables from a `.env` file.

### 📦 Deployment & Hosting
- **Render.com** - Hosting the Django web application.

### 🛠️ Development & DevOps Tools
- **Git & GitHub** - Version control and collaboration.
- **VS Code / PyCharm** - IDEs for coding and debugging.

---

## ⚙️ Installation & Setup  

### 1️⃣ **Clone the Repository**
```bash
git clone https://github.com/zeynepsevvalsener/se3355-final-car-rental.git
cd se3355-final-car-rental
