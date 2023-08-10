class Employee:
    def __init__(self, emp_name, emp_num):
        self.__emp_name = emp_name
        self.__emp_num = emp_num

    def get_emp_name(self):
        return self.__emp_name

    def set_emp_name(self, emp_name):
        self.__emp_name = emp_name

    def get_emp_num(self):
        return self.__emp_num

    def set_emp_num(self, emp_num):
        self.__emp_num = emp_num

