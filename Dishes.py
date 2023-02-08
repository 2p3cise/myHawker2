
import random 
class Dish:
    count_id = None

    def __init__(self, dish_name, price, description):
        Dish.count_id = random.randint(0,1000)
        self.__dish_id = Dish.count_id
        self.__dish_name = dish_name
        self.__price = price
        self.__description = description

    def get_dish_id(self):
        return self.__dish_id

    def get_dish_name(self):
        return self.__dish_name

    def get_price(self):
        return self.__price

    def get_description(self):
        return self.__description

    def set_dish_id(self, dish_id):
        self.__dish_id = dish_id

    def set_dish_name(self, dish_name):
        self.__dish_name = dish_name

    def set_price(self, price):
        self.__price = price

    def set_description(self, description):
        self.__description = description
