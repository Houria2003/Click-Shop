# 🛍️ Flask E-commerce Website (with Docker)

A complete e-commerce website built with **Flask**, using **SQLAlchemy** for database management and **HTML/CSS/JavaScript** on the frontend. This project includes user authentication, product search, cart functionality, order placement, and an admin section for managing products and orders.

---

## ✅ Features

- Customers can sign in or sign up
- Customers can reset their passwords
- Customers can search for products
- Customers can add items to the cart
- Customers can place orders
- Admins can manage shop products and stock
- Admins can change the status of orders

---

## 🧰 Tech Stack

- **Backend**: Python (Flask), SQLAlchemy
- **Frontend**: HTML, CSS, JavaScript
- **Containerization**: Docker

---

📦 How to Run with Docker

docker pull linamrsl20/ecommerce-flask:latestdocker run -itd -p 8034:5000 linamrsl20/ecommerce-flask:latesthttp://localhost:8034

🐍 Local Development 

git clone https://github.com/yourusername/Flask-Ecommerce.gitcd Flask-Ecommercepython -m venv venvsource venv/bin/activatepip install -r requirements.txtpython main.pyhttp://localhost:5000

