from Saloon.app import app
from Saloon.database import connect_db
from flask import redirect
from datetime import datetime
from flask import request, render_template


@app.route('/')
def homepage():
    return render_template('main.html')


@app.route('/services.html')
def get_services():
    db = connect_db()
    cur = db.cursor()
    cur.execute('select * from services')
    items = cur.fetchall()
    return render_template('services.html', pricing=items)


# перенеси все  что свзяано с бд отсюда в файл бд и сделай вызов ищ модели чтоб красиво все было и гибко
@app.route('/addservice.html', methods=['GET', 'POST'])
def add_service():
    if request.method == "GET":
        return render_template('addservice.html')
    sex = request.form['sex']
    service = request.form['service']
    name = request.form['name']
    price = request.form['price']
    db = connect_db()
    db.execute(
        'insert into services (sex,service,name,price) values(?,?,?,?)',
        [sex, service, name, price]
    )
    db.commit()
    return redirect('/')


@app.route('/customers.html')
def customers():
    db = connect_db()
    cur = db.cursor()
    cur.execute('select * from customers')
    customer = cur.fetchall()
    return render_template('customers.html', customers=customer)


@app.route('/addcustomer.html', methods=['GET', 'POST'])
def addcustomer():
    if request.method == 'GET':
        return render_template('addcustomer.html')
    name = request.form['name']
    surname = request.form['surname']
    db = connect_db()
    db.execute('insert into customers (name,surname) values (?,?)', [name, surname])
    db.commit()
    return redirect('customers.html')


@app.route('/journal.html', methods=['GET'])
def journal():
    db = connect_db()
    cur = db.cursor()
    cur.execute('select j.date,customer.name,customer.surname,s.name,s.price,s.service from journal j join customers '
                'customer on j.name = customer.id '
                'join services s on j.service = s.id')
    item = cur.fetchall()
    item = list(map(list, item))
    for position in item:
        position[0] = (datetime.utcfromtimestamp(int(position[0])).strftime('%d-%m-%Y '))
    return render_template('journal.html', items=item)
