from wtforms import Form, StringField, RadioField, SelectField, TextAreaField, validators,FloatField, DecimalField, ValidationError, PasswordField

class CreateDishForm(Form):
    dish_name = StringField('Dish Name', [validators.Length(min=1, max=150), validators.DataRequired()])
    price = DecimalField('Price', [validators.DataRequired()])
    description = TextAreaField('Description', [validators.Length(min=10, max=1024), validators.DataRequired()])

    def validate_dish_name(form, dish_name):
        if not form.dish_name.data.isalpha():
            raise ValidationError("Dish Name cannot contain numbers")

    def validate_price(form, price):
        if form.price.data < 0:
            raise ValidationError("Cannot input negative numbers!")

class CreateCustomerForm(Form):
    customer_name = StringField('Customer Name', [validators.Length(min=1, max=100), validators.DataRequired()])
    password = PasswordField('Password', [validators.DataRequired()])