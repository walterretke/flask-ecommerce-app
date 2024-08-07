﻿# flask-ecommerce-app

Description
flask-ecommerce-app is a fully functional ecommerce application built using Python, Flask, and SQLite. This project provides a robust foundation for developing a scalable online store, featuring user authentication, product management, a shopping cart, and order processing. Designed with simplicity and flexibility in mind, it is ideal for developers looking to create or expand their ecommerce solutions.

Features
User Authentication: Secure user registration and login system with password hashing.
Product Management: Admin interface for adding, editing, and deleting products.
Shopping Cart: Users can add products to the cart, view their cart, and proceed to checkout.
Order Processing: Complete order workflow including order summary and confirmation.
Database Integration: Utilizes SQLite for easy setup and management of the database.
Responsive Design: Mobile-friendly interface for a seamless shopping experience across devices.
RESTful API: Provides endpoints for integration with other services or front-end frameworks.
Installation
Clone the Repository:

bash
Copiar código
git clone https://github.com/yourusername/flask-ecommerce-app.git
cd flask-ecommerce-app
Create a Virtual Environment:

bash
Copiar código
python3 -m venv venv
source venv/bin/activate   # On Windows use `venv\Scripts\activate`
Install Dependencies:

bash
Copiar código
pip install -r requirements.txt
Set Up the Database:

bash
Copiar código
flask db init
flask db migrate -m "Initial migration"
flask db upgrade
Run the Application:

bash
Copiar código
flask run
Usage
Navigate to http://127.0.0.1:5000 in your web browser to access the application.
Use the admin interface to manage products and view orders.
Explore the API endpoints via http://127.0.0.1:5001/api.
Contributing
Contributions are welcome! Please fork the repository and submit pull requests for any enhancements or bug fixes.
