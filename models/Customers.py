#Nicholas
import shelve


class Customer:
    count_id = None

    def __init__(self, first_name, last_name, gender, email, date_joined, address, password):
        with shelve.open("counter", writeback=True) as counter:
            if "customers" not in counter:
                id = 1
            else:
                id = counter["customers"] + 1
            
            counter["customers"] = id
        self.__customer_id = id
        self.__first_name = first_name
        self.__last_name = last_name
        self.__gender = gender
        self.__email = email
        self.__date_joined = date_joined
        self.__address = address
        self.__password = password

    # accessor methods
    def get_customer_id(self):
        return self.__customer_id
    
    def get_first_name(self):
        return self.__first_name

    def get_last_name(self):
        return self.__last_name

    def get_gender(self):
        return self.__gender

    def get_email(self):
        return self.__email

    def get_date_joined(self):
        return self.__date_joined

    def get_address(self):
        return self.__address

    def get_password(self):
        return self.__password

    # mutator methods
    
    def set_customer_id(self, customer_id):
        self.__customer_id = customer_id

    def set_first_name(self, first_name):
        self.__first_name = first_name

    def set_last_name(self, last_name):
        self.__last_name = last_name

    def set_gender(self, gender):
        self.__gender = gender

    def set_email(self, email):
        self.__email = email

    def set_address(self, address):
        self.__address = address

    def set_date_joined(self, date_joined):
        self.__date_joined = date_joined

    def set_password(self, password):
        self.__password = password