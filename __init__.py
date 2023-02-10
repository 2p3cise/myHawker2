from flask import Flask, render_template, request, redirect, url_for
from Forms import CreateDishForm, CreateCustomerForm
import shelve, Dishes, Customers

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/contactUs')
def contact_us():
    return render_template('contactUs.html')

@app.route('/createDish', methods=['GET', 'POST'])
def create_dish():
    create_dish_form = CreateDishForm(request.form)
    if request.method == 'POST' and create_dish_form.validate():
        dishes_dict = {}
        db = shelve.open('dish.db', 'c')

        try:
            dishes_dict = db['Dishes']
        except:
            print("Error in retrieving Users from dish.db")

        dish = Dishes.Dish(create_dish_form.dish_name.data, create_dish_form.price.data, create_dish_form.description.data, create_dish_form.cuisine.data)
        dishes_dict[dish.get_dish_id()] = dish
        db['Dishes'] = dishes_dict

        db.close()

        return redirect(url_for('retrieve_dishes'))
    return render_template('createDish.html', form=create_dish_form)


@app.route('/retrieveDish')
def retrieve_dishes():
    dishes_dict = {}
    db = shelve.open('dish.db', 'r')
    dishes_dict = db['Dishes']
    db.close()

    dishes_list = []
    for key in dishes_dict:
        dish = dishes_dict.get(key)
        dishes_list.append(dish)

    return render_template('retrieveDish.html', count=len(dishes_list), dishes_list=dishes_list)


@app.route('/updateDish/<int:id>/', methods=['GET', 'POST'])
def update_dish(id):
    update_dish_form = CreateDishForm(request.form)
    if request.method == 'POST' and update_dish_form.validate():
        dishes_dict = {}
        db = shelve.open('dish.db', 'w')
        dishes_dict = db['Dishes']

        dish = dishes_dict.get(id)
        dish.set_dish_name(update_dish_form.dish_name.data)
        dish.set_price(update_dish_form.price.data)
        dish.set_description(update_dish_form.description.data)
        dish.set_cuisine(update_dish_form.cuisine.data)

        db['Dishes'] = dishes_dict
        db.close()

        return redirect(url_for('retrieve_dishes'))
    else:
        dishes_dict = {}
        db = shelve.open('dish.db', 'r')
        dishes_dict = db['Dishes']
        db.close()

        dish = dishes_dict.get(id)
        update_dish_form.dish_name.data = dish.get_dish_name()
        update_dish_form.price.data = dish.get_price()
        update_dish_form.description.data = dish.get_description()
        update_dish_form.cuisine.data = dish.get_cuisine()

        return render_template('updateDish.html', form=update_dish_form)


@app.route('/deleteDish/<int:id>', methods=['POST'])
def delete_dish(id):
    dishes_dict = {}
    db = shelve.open('dish.db', 'w')
    dishes_dict = db['Dishes']
    dishes_dict.pop(id)
    db['Dishes'] = dishes_dict
    db.close()
    return redirect(url_for('retrieve_dishes'))

@app.route('/addtocart/<int:id>', methods=['POST'])
def add_to_cart(id):
    dishes_dict = {}
    db = shelve.open('dish.db', 'w')
    dishes_dict = db['Dishes']
    dishes_dict.pop(id)
    db['Dishes'] = dishes_dict
    db.close()
    return redirect(url_for('retrieve_dishes'))


@app.route('/adminindiancuisine')
def adminindian_cuisine():
    dishes_dict = {}
    db = shelve.open('dish.db', 'r')
    dishes_dict = db['Dishes']
    db.close()

    dishes_list = []
    for key in dishes_dict:
        dish = dishes_dict.get(key)
        dishes_list.append(dish)

    return render_template('adminindiancuisine.html', count=len(dishes_list), dishes_list=dishes_list)

@app.route('/customerindiancuisine')
def customerindian_cuisine():
    dishes_dict = {}
    db = shelve.open('dish.db', 'r')
    dishes_dict = db['Dishes']
    db.close()

    dishes_list = []
    for key in dishes_dict:
        dish = dishes_dict.get(key)
        dishes_list.append(dish)

    return render_template('customerindiancuisine.html', count=len(dishes_list), dishes_list=dishes_list)

@app.route('/westerncuisine')
def western_cuisine():
    dishes_dict = {}
    db = shelve.open('dish.db', 'r')
    dishes_dict = db['Dishes']
    db.close()

    dishes_list = []
    for key in dishes_dict:
        dish = dishes_dict.get(key)
        dishes_list.append(dish)

    return render_template('westerncuisine.html', count=len(dishes_list), dishes_list=dishes_list)




@app.route('/registering', methods=['GET', 'POST'])
def create_customer():
    create_customer_form = CreateCustomerForm(request.form)
    if request.method == 'POST' and create_customer_form.validate():
        customers_dict = {}
        db = shelve.open('customers.db', 'c')

        try:
            customers_dict = db['Customers']
        except:
            print("Error in retrieving Users from customers.db")

        customer = Customers.Customer(create_customer_form.customer_name.data, create_customer_form.password.data)
        customers_dict[customer.get_customer_id()] = customer
        db['Customers'] = customers_dict

        db.close()

        return redirect(url_for('retrieve_customers'))
    return render_template('registering.html', form=create_customer_form)



@app.route('/retrieveCustomer')
def retrieve_customers():
    customers_dict = {}
    db = shelve.open('customers.db', 'r')
    customers_dict = db['Customers']
    db.close()

    customers_list = []
    for key in customers_dict:
        customer = customers_dict.get(key)
        customers_list.append(customer)

    return render_template('retrieveCustomer.html', count=len(customers_list), customers_list=customers_list)

@app.route('/updateCustomer/<int:id>/', methods=['GET', 'POST'])
def update_customer(id):
    update_customer_form = CreateCustomerForm(request.form)
    if request.method == 'POST' and update_customer_form.validate():
        customers_dict = {}
        db = shelve.open('customers.db', 'w')
        customers_dict = db['Customers']

        customer = customers_dict.get(id)
        customer.set_customer_name(update_customer_form.customer_name.data)
        customer.set_password(update_customer_form.password.data)

        db['Customers'] = customers_dict
        db.close()

        return redirect(url_for('retrieve_customers'))
    else:
        customers_dict = {}
        db = shelve.open('customers.db', 'r')
        customers_dict = db['Customers']
        db.close()

        customer = customers_dict.get(id)
        update_customer_form.customer_name.data = customer.get_customer_name()
        update_customer_form.password.data = customer.get_password()

        return render_template('updateCustomer.html', form=update_customer_form)

@app.route('/deleteCustomer/<int:id>', methods=['POST'])
def delete_customer(id):
    customers_dict = {}
    db = shelve.open('customers.db', 'w')
    customers_dict = db['Customers']
    customers_dict.pop(id)
    db['Customers'] = customers_dict
    db.close()
    return redirect(url_for('retrieve_customers'))


if __name__ == '__main__':
    app.run(debug=True)
