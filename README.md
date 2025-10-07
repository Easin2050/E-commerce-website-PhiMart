# 🛒 PhiMart – E-Commerce REST API  

A **scalable E-Commerce REST API** built with **Django REST Framework (DRF)**.  
It provides **JWT Authentication, product & category management, shopping carts, orders, and reviews** – everything you need to power an online store backend.  

<p align="center">
  <img src="https://img.shields.io/badge/Django-4.x-green?style=for-the-badge&logo=django" />
  <img src="https://img.shields.io/badge/DRF-3.x-red?style=for-the-badge&logo=django" />
  <img src="https://img.shields.io/badge/PostgreSQL-15-blue?style=for-the-badge&logo=postgresql" />
  <img src="https://img.shields.io/badge/Swagger-API Docs-orange?style=for-the-badge&logo=swagger" />
</p>

---

## ✨ Features  

- 🔐 **Authentication & Authorization**  
  - JWT authentication via [Djoser](https://djoser.readthedocs.io/en/latest/)  
  - Secure user registration & login  

- 📦 **Products & Categories**  
  - Create, update, delete products  
  - Organize with categories  

- 🛒 **Shopping Cart**  
  - Add, update, and remove cart items  
  - View user’s active cart  

- ⭐ **Product Reviews**  
  - Customers can leave reviews  
  - Only verified users can review  

- 📑 **Orders Management**  
  - Place new orders  
  - Update or cancel orders  
  - Track order history  

- 📖 **Interactive API Documentation**  
  - Swagger UI & Redoc powered by **drf-spectacular / drf-yasg**  

---

## 🏗️ Tech Stack  

- **Backend:** Django, Django REST Framework  
- **Authentication:** JWT via Djoser  
- **Database:** PostgreSQL (recommended) | SQLite (for development)  
- **API Docs:** Swagger / Redoc (drf-spectacular, drf-yasg)  
- **Other Tools:** Git  

---

## 🚀 Installation & Setup  

### 1️⃣ Clone the repository  
```bash
git clone https://github.com/Easin2050/E-commerce-website-PhiMart.git
cd phiMart
```

### 2️⃣ Create a virtual environment & activate it

python -m venv .phi_env

## Linux / Mac
source .phi_env/bin/activate  
## Windows
.phi_env\Scripts\activate

### 3️⃣ Install dependencies
pip install -r requirements.txt

### 4️⃣ Run migrations
python manage.py migrate

### 5️⃣ Start the development server

python manage.py runserver

### 📚 API Documentation

After starting the server, explore API docs at:

Swagger UI: http://127.0.0.1:8000/swagger/

Redoc: http://127.0.0.1:8000/redoc/
