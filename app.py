#importacao
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS
from flask_login import UserMixin, login_user, LoginManager, login_required, logout_user

#criacao do app
app = Flask(__name__)

#database config e conexao
app.config['SECRET_KEY'] = "minha_chave_123"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ecommerce.db'

login_manager = LoginManager()
db = SQLAlchemy(app)
login_manager.init_app(app)
login_manager.login_view = 'login'
CORS(app)
migrate = Migrate(app, db)

#modelagem

#usuario

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), nullable=False, unique=True)
    password = db.Column(db.String(80), nullable=False)

#rotas

@app.route('/login', methods=["POST"])
def app_login():
    data = request.json

    user = User.query.filter_by(username=data.get("username")).first()
    if user and data.get("password") == user.password:
            login_user(user)
            return jsonify({"message": "Logged in successfully"}), 200
    return jsonify({"message": "User not found"}), 404

@app.route('/logout', methods=["POST"])
@login_required
def app_logout():
    logout_user()
    return jsonify({"message": "Logout in successfully"}), 200

#produto(id, name, price, descritpion)

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    price = db.Column(db.Float, nullable=False)
    description = db.Column(db.Text, nullable=True)

#rotas (/api/modelousado/funcao)

#autenticaco
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
    # ADD
@app.route('/api/product/add', methods=["POST"])
@login_required
def add_new_product():
    data = request.json
    if 'name' in data and 'price' in data:
        product = Product(name=data["name"],price=data["price"],description=data.get("description", ""))
        db.session.add(product)
        db.session.commit()
        return jsonify({"message": "Product added successfully"}), 200
    return jsonify({"message": "Invalid product data"}), 400

    #DELETE
@app.route('/api/product/delete/<int:product_id>', methods=["DELETE"])
@login_required
def delete_product(product_id):
    product = Product.query.get(product_id)
    if product:
        db.session.delete(product)
        db.session.commit()
        return jsonify({"message": "Product deleted successully"}), 200
    return jsonify({"message": "Product not found"}), 404

    #GET ITEMS
@app.route('/api/product/<int:product_id>', methods=["GET"])
def get_product_details(product_id):
    product = Product.query.get(product_id)
    if product:
        return jsonify({
            "id": product.id,
            "name": product.name,
            "price": product.price,
            "description": product.description
        }), 200
    return jsonify({"message": "Product not found"}), 404

    #UPDATE
@app.route('/api/product/update/<int:product_id>', methods=["PUT"])
@login_required
def update_product(product_id):
    product = Product.query.get(product_id)
    if not product:
        return jsonify({"message": "Product not found"}), 404
    data = request.json
    if 'name' in data:
        product.name = data['name']
    if 'price' in data:
        product.price = data['price']
    if 'description' in data:
        product.description = data['description']
    
    db.session.commit()
    return jsonify({"message": "Product updated successfully"})

    #LIST PRODUCTS
@app.route('/api/products', methods=["GET"])
def list_all_products():
    products = Product.query.all()
    products_list = []
    for product in products:
        products_data = {
            "id": product.id,
            "name": product.name,
            "price": product.price,
            "description": product.description
        }
        products_list.append(products_data)

    return jsonify(products_list)

#rota raiz (inicial)
@app.route('/')
def hello_world():
    return 'Hello World'

if __name__ == "__main__":
    app.run(debug=True, port=5001)