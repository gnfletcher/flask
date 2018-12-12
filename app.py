from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import IntegrityError, InvalidRequestError
from base import BASE
from product import Product
from shoppingcart import ShoppingCart
from wishlist import Wishlist
from customers import Customers
from sakilaCustomers import SakilaCustomers
from sakilaProducts import SakilaProducts
from inventory import Inventory
from suppliers import Suppliers
import datetime;

connection = create_engine('mysql+pymysql://guest:guest@localhost:3306/db_project')
sakilaconnection = create_engine('mysql+pymysql://guest:guest@localhost:3306/sakila')
BASE.metadata.create_all(connection)
BASE.metadata.create_all(sakilaconnection)

Session = sessionmaker(bind=connection)
Session2 = sessionmaker(bind=sakilaconnection)
session = Session()
session2 = Session2()
session.rollback()
session2.rollback()


@app.route('/')
def index():
    return render_template('main.html')


@app.route('/Admin')
def adminpage():
    return render_template('admin.html')


@app.route('/Sakila')
def sakilapage():

    return render_template('sakila.html')


@app.route('/Sakila/Customers')
def sakilacustomerspage():
    customers = session2.query(SakilaCustomers).all()
    return render_template('customers.html', customers=customers)

@app.route('/Sakila/Products')
def sakilaproductspage():
    products = session2.query(SakilaProducts).all()
    return render_template('films.html', products=products)


@app.route('/Inventory')
def getinventory():
    inventory = session.query(Inventory).all()
    return render_template('inventory.html', inventory=inventory)


@app.route('/Customers')
def customerspage():
    customers = session.query(Customers).all()
    return render_template('customers.html', customers=customers)


@app.route('/Suppliers')
def getsuppliers():
    suppliers = session.query(Suppliers).all()
    return render_template('suppliers.html', suppliers=suppliers)


@app.route('/Products')
def getproducts():
    products = session.query(Product).all()
    return render_template('Products.html', products=products)


@app.route('/product/<int:product_id>/')
def getProduct(product_id):
    product = session.query(Product).filter_by(product_id=product_id).one()
    return render_template('Product.html', product=product)


@app.route('/products/new/', methods=['GET', 'POST'])
def insertProduct():
    if request.method == 'POST':
        product_id = request.form['product_id']
        name = request.form['name']
        description = request.form['description']
        price = request.form['price']
        newproduct = Product(product_id=product_id, name=name, description=description, price=price)
        session.add(newproduct)
        session.commit()
        flash("new product " + name + " created")
        return redirect(url_for('getProducts'))
    else:
        return render_template('newproduct.html')


@app.route('/products/<int:actor_id>/update/', methods=['GET', 'POST'])
def updateProduct(product_id):
    editedProduct = session.query(Product).filter_by(product_id=product_id).one()
    if request.method == 'POST':
        name = request.form['name']
        description = request.form['description']
        price = request.form['price']
        editedProduct.name = name
        editedProduct.description = description
        editedProduct.price = price
        session.add(editedProduct)
        session.commit()
        flash(name + "'s information updated")
        return redirect(url_for('getProducts'))
    else:
        return render_template('editproduct.html', product=editedProduct)


@app.route('/products/<int:actor_id>/delete/', methods=['GET', 'POST'])
def deleteProduct(product_id):
    deletedproduct = session.query(Product).filter_by(product_id=product_id).one()
    if request.method == 'POST':
        session.delete(deletedproduct)
        session.commit()
        flash(deletedproduct.name + " deleted")
        return redirect(url_for('getProducts'))
    else:
        return render_template('deleteproduct.html', product=deletedproduct)


@app.route('/ShoppingCart')
def getShoppingCart():
    shoppingcart = session.query(ShoppingCart).all()
    return render_template('shoppingcart.html', shoppingcart = shoppingcart)


@app.route('/ShoppingCart/add')
def addShoppingCart(shoppingcart, customer_id, product_id, quantity):
    if request.method == 'POST':
        newshoppingcart = session.execute('add_to_cart', customer_id=customer_id, product_id=product_id, quantity=quantity)
        session.commit()
        flash(product_id + " added to cart")
        return render_template('shoppingcart.html', shoppingcart=shoppingcart)
    else:
        return render_template('shoppingcart.html', shoppingcart=shoppingcart)


@app.route('/Wishlist')
def getWishlist():
    wishlist = session.query(Wishlist).all()
    return render_template('wishlist.html', wishlist = wishlist)


if __name__ == '__main__':
    app.run()
