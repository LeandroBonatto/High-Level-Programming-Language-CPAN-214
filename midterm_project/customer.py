from person import Person

class Customer(Person):
    def __init__(self, name, address, phone_num, customer_num, mailing_list=True):
        super().__init__(name, address, phone_num)
        self.__customer_num = customer_num
        self.__mailing_list = mailing_list

    def get_customer_num(self):
        return self.__customer_num

    def set_customer_num(self, customer_num):
        self.__customer_num = customer_num

    def get_mailing_list(self):
        return self.__mailing_list

    def set_mailing_list(self, mailing_list):
        self.__mailing_list = mailing_list

def main():
    cust = Customer("Johnny C.", "52 Humber Street", "416-555-2552", 4787, True)
    print('=== Customer Info ==='
          '\nName: {} '
          '\nAddress: {} '
          '\nPhone Number: {} '
          '\nCustomer Number: {} '
          '\nWish mailing list: {}'.format(cust.get_name(), cust.get_address(), cust.get_phone_num(),
                                                        cust.get_customer_num(), cust.get_mailing_list()))

main()