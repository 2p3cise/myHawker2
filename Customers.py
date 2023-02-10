import random 
class Customer:
    count_id = None

    def __init__(self, customer_name, password):
        Customer.count_id = random.randint(0,1000)
        self.__customer_id = Customer.count_id
        self.__customer_name = customer_name
        self.__password = password

    def get_customer_id(self):
        return self.__customer_id

    def get_customer_name(self):
        return self.__customer_name

    def get_password(self):
        return self.__password


    def set_customer_id(self, customer_id):
        self.__customer_id = customer_id

    def set_customer_name(self,customer_name):
        self.__customer_name = customer_name

    def set_password(self, password):
        self.__password = password