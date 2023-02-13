from models.Dishes import Dish


class Cart(Dish):
    def __init__(self, dish_name, price, quantity):
        super(Cart, self).__init__(dish_name, price)
        self.__quantity = quantity

    def get_quantity(self):
        return self.__quantity

    def set_quantity(self, quantity):
        self.__quantity = quantity
