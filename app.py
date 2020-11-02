import random
import string
import flask_sijax
from flask import Flask, render_template, flash, redirect, url_for, session, request, logging, g
from flask_mysqldb import MySQL
from wtforms import Form, StringField, TextAreaField, PasswordField, validators, SelectField
from passlib.hash import sha256_crypt
from functools import wraps
from flask_uploads import UploadSet, configure_uploads, IMAGES
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)
# Config MySQL
mysql = MySQL()
app.config['MYSQL_HOST'] = '127.0.0.1'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '1234'
app.config['MYSQL_DB'] = 'project3'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
mysql.init_app(app)


@app.route('/AdminLogin', methods=["POST"])
def AdminLogin():
    rememberme = request.form.get('remember')
    if request.method == 'POST':
        email = request.form['user']
        password = request.form['pass'].encode('utf-8')
        curl = mysql.connection.cursor()
        curl.execute("SELECT * FROM admin WHERE username=%s", (email,))
        user = curl.fetchone()
        curl.close()
        if len(user) > 0:
            if user["password"].encode('utf-8') == password:
                if rememberme == "checked":
                    session['loggin'] = True
                return render_template('AdminHomepage.html')
            else:
                return render_template("homepage.html",
                msg="Wrong username or password, please try again!")
        else:
            return render_template("homepage.html")
            return "Error user not found"
    else:
        return render_template("homepage.html")


def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'loggin' in session:
            return f(*args, **kwargs)
        else:
            flash('SORRY You Need To Login First', 'danger')
            return redirect(url_for('home'))

    return decorated_function


@app.route('/deleteP/<string:id>', methods=["POST"])
@login_required
def deleteP(id):
    if request.method == "POST":
        cursor = mysql.connection.cursor()
        cursor.execute("DELETE FROM product WHERE id=%s", (id,))
        mysql.connection.commit()
        flash(f'Product with id:{id} has been deleted successfully', 'success')
        return redirect(url_for('admin'))


@app.route('/edit/<string:id>', methods=["POST"])
@login_required
def edit(id):
    if request.method == "POST":
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT * FROM product WHERE id=%s", (id,))
        row = cursor.fetchall()
        return render_template("Edit product.html", products=row)


@app.route('/editP/<string:id>', methods=["POST"])
@login_required
def editP(id):
    quantity = int(request.form['quantity'])
    pic = request.form['pimage']
    name = request.form['name']
    des = request.form['description']
    price = float(request.form['price'])
    try:
        if name and request.method == 'POST':
            cursor = mysql.connection.cursor()
            cursor.execute(" UPDATE product SET name = %s WHERE id = %s", (name, id,))
            mysql.connection.commit()
        if pic and request.method == 'POST':
            cursor = mysql.connection.cursor()
            cursor.execute(" UPDATE product SET pic = %s WHERE id = %s", (pic, id,))
            mysql.connection.commit()
        if price and request.method == 'POST':
            cursor = mysql.connection.cursor()
            cursor.execute(
                " UPDATE product SET price = %s WHERE id = %s", (price, id,))
            mysql.connection.commit()
        if des and request.method == 'POST':
            cursor = mysql.connection.cursor()
            cursor.execute(
                " UPDATE product SET Description = %s WHERE id = %s", (des, id,))
            mysql.connection.commit()
        if price and request.method == 'POST':
            cursor = mysql.connection.cursor()
            cursor.execute(
                " UPDATE product SET price = %s WHERE id = %s", (price, id,))
            mysql.connection.commit()
        if price and request.method == 'POST':
            cursor = mysql.connection.cursor()
            cursor.execute(" UPDATE product SET NO_item = %s WHERE id = %s", (quantity, id,))
            mysql.connection.commit()

        flash(f'Product with id:{id} has been edited successfully', 'success')
        return redirect(url_for('admin'))

    except Exception as e:
        print(e)


@app.route('/addProduct')
@login_required
def addP():
    return render_template("addproduct.html")


@app.route('/addProduct1', methods=['POST'])
@login_required
def addProduct():
    try:
        quantity = int(request.form['q'])
        pic = request.form['image']
        name = request.form['name']
        cat = request.form['cat']
        type1 = request.form['type']
        des = request.form['dis']
        price = float(request.form['price'])

        if name and pic and price and quantity and request.method == 'POST':
            cursor = mysql.connection.cursor()
            cursor.execute(
                " INSERT INTO product (id,name, type, category, price, NO_item, pic, Description) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)",
                (randomString(), name, type1, cat, price, quantity, pic, des,))
            mysql.connection.commit()
            flash(f'A new product with id:{randomString()} has been added successfully', 'success')

            return redirect(url_for('admin'))
    except Exception as e:
        print(e)


@app.route('/logout')
@login_required
def logout():
    session.pop('loggin', None)
    flash('You were logged out.', 'success')
    return redirect(url_for('home'))


@app.route('/admin', methods=['GET', 'POST'])
@login_required
def admin():
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM product ORDER BY id ASC")
    rows = cursor.fetchall()
    return render_template("AdminHomepage.html", products=rows)


@app.route('/')
def home():
    return render_template("homepage.html")


@app.route('/fresh', methods=['GET', 'POST'])
def fresh():
    cursor = mysql.connection.cursor()
    values = 'fresh'
    cursor.execute("SELECT * FROM product WHERE category=%s ORDER BY id ASC", (values,))
    rows = cursor.fetchall()
    return render_template("product.html", fresh=rows)


@app.route('/organic', methods=['GET', 'POST'])
def organic():
    cursor = mysql.connection.cursor()
    values = 'OrganicFood'
    cursor.execute("SELECT * FROM product WHERE category=%s ORDER BY id ASC", (values,))
    rows = cursor.fetchall()
    return render_template("product.html", fresh=rows)


@app.route('/FoodBeverages', methods=['GET', 'POST'])
def food():
    cursor = mysql.connection.cursor()
    values = 'FoodBeverages'
    cursor.execute("SELECT * FROM product WHERE category=%s ORDER BY id ASC", (values,))
    rows = cursor.fetchall()
    return render_template("product.html", fresh=rows)

@app.route('/checkout', methods=['GET', 'POST'])
def checkout():
    if 'cart_item' not in session:
        return render_template("checkout.html")
    else:
        subtotal = 0
        totalQ = 0
        total = 0
        cursor = mysql.connection.cursor()

        for key, product in session['cart_item'].items():
            cursor.execute("SELECT NO_item FROM product WHERE id=%s ", (product['id'],))
            rows = cursor.fetchone()
            subtotal += float(product['price']) * int(product['quantity'])
            totalQ += int(product['quantity'])
            total = subtotal

        return render_template("checkout.html", total=total, totalQ=totalQ, maxQ=rows)


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    return render_template("contact.html")

@app.route('/details/<string:id>')
def details(id):
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM product WHERE id=%s", (id,))
    row = cursor.fetchall()
    return render_template("product-detail.html", products=row)


@app.route('/empty')
def empty_cart():
    try:
        session.clear()
        return redirect(request.referrer)
    except Exception as e:
        print(e)


@app.route('/delete/<string:id>')
def delete_product(id):
    try:
        all_total_price = 0
        all_total_quantity = 0
        session.modified = True
        for item in session['cart_item'].items():
            if item[0] == id:
                session['cart_item'].pop(item[0], None)
                if 'cart_item' in session:
                    for key, value in session['cart_item'].items():
                        individual_quantity = int(session['cart_item'][key]['quantity'])
                        individual_price = float(session['cart_item'][key]['total_price'])
                        all_total_quantity = all_total_quantity + individual_quantity
                        all_total_price = all_total_price + individual_price
                break
        if all_total_quantity == 0:
            session.clear()
        else:
            session['all_total_quantity'] = all_total_quantity
            session['all_total_price'] = all_total_price
        return redirect(url_for('.checkout'))
    except Exception as e:
        print(e)


@app.route('/buy')
def buy():
    try:
        cursor = mysql.connection.cursor()

        for key, product in session['cart_item'].items():

            cursor.execute("UPDATE product SET NO_item = NO_item-%s WHERE id = %s", (int(product['quantity']), product['id'],))
            mysql.connection.commit()

        session.clear()
        flash(' Thank you, your order has been confirmed successfully', 'success')
        return redirect(url_for('home'))
    except Exception as e:
        print(e)


@app.route('/update/<string:id>', methods=['POST'])
def update_product(id):
    all_total_price = 0
    all_total_quantity = 0
    if request.method == "POST":
        _quantity = int(request.form['quantity'])
        try:
            session.modified = True
            for key, item in session['cart_item'].items():
                if key == id:
                    item['quantity'] = _quantity
                    individual_quantity = int(session['cart_item'][key]['quantity'])
                    individual_price = float(session['cart_item'][key]['total_price'])
                    all_total_quantity = all_total_quantity + individual_quantity
                    all_total_price = all_total_price + individual_price

            session['all_total_quantity'] = all_total_quantity
            session['all_total_price'] = all_total_price
            return redirect(request.referrer)
        except Exception as e:
            print(e)
            return redirect(request.referrer)


@app.route('/add', methods=['POST'])
def addCart():
    try:
        _quantity = int(request.form['quantity'])
        _code = request.form['id']
        if _quantity and _code and request.method == 'POST':
            cursor = mysql.connection.cursor()
            cursor.execute("SELECT * FROM product WHERE id=%s", (_code,))
            row = cursor.fetchone()
            itemArray = {
                row['id']: {'name': row['name'], 'id': row['id'], 'quantity': _quantity, 'price': row['price'],
                            'image': row['pic'], 'total_price': _quantity * row['price']}}
            all_total_price = 0
            all_total_quantity = 0
            session.modified = True
            if 'cart_item' in session:
                if row['id'] in session['cart_item']:
                    for key, value in session['cart_item'].items():
                        if row['id'] == key:
                            old_quantity = session['cart_item'][key]['quantity']
                            total_quantity = old_quantity + _quantity
                            session['cart_item'][key]['quantity'] = total_quantity
                            session['cart_item'][key]['total_price'] = total_quantity * row['price']
                else:
                    session['cart_item'] = array_merge(session['cart_item'], itemArray)

                for key, value in session['cart_item'].items():
                    individual_quantity = int(session['cart_item'][key]['quantity'])
                    individual_price = float(session['cart_item'][key]['total_price'])
                    all_total_quantity = all_total_quantity + individual_quantity
                    all_total_price = all_total_price + individual_price
            else:
                session['cart_item'] = itemArray
                all_total_quantity = all_total_quantity + _quantity
                all_total_price = all_total_price + _quantity * row['price']
            session['all_total_quantity'] = all_total_quantity
            session['all_total_price'] = all_total_price
            return redirect(request.referrer)
        else:
            return 'Error while adding item to cart+"_code" '
    except Exception as e:
        print(e)


def array_merge(first_array, second_array):
    if isinstance(first_array, list) and isinstance(second_array, list):
        return first_array + second_array
    elif isinstance(first_array, dict) and isinstance(second_array, dict):
        return dict(list(first_array.items()) + list(second_array.items()))
    elif isinstance(first_array, set) and isinstance(second_array, set):
        return first_array.union(second_array)
    return False


def randomString(stringLength=5):
    """Generate a random string of fixed length """
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))
