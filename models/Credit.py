# Ryan
class Credit:

    def __init__(self, credit_card_num, cvc, expiry_date):
        self.__credit_card_num = credit_card_num
        self.__cvc = cvc
        self.__expiry_date = expiry_date

    def get_credit_card_num(self):
        return self.__credit_card_num

    def set_credit_card_num(self, credit_card_num):
        self.__credit_card_num = credit_card_num

    def get_cvc(self):
        return self.__cvc

    def set_cvc(self, cvc):
        self.__cvc = cvc

    def get_expiry_date(self):
        return self.__expiry_date

    def set_expiry_date(self, expiry_date):
        self.__expiry_date = expiry_date
