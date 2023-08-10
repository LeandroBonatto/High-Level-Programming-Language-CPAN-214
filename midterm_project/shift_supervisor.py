from company_people import Employee

class ShiftSupervisor(Employee):
    def __init__(self, emp_name, emp_num, annual_salary, yearly_bonus):
        super().__init__(emp_name, emp_num)
        self.__annual_salary = annual_salary
        self.__yearly_bonus = yearly_bonus

    def get_annual_salary(self):
        return self.__annual_salary

    def set_annual_salary(self, annual_salary):
        self.__annual_salary = annual_salary

    def get_yearly_bonus(self):
        return self.__yearly_bonus

    def set_yearly_bonus(self, yearly_bonus):
        self.__yearly_bonus = yearly_bonus

def main():
    super = ShiftSupervisor("Caio", 477, 22000, 2350)
    print('Supervisor attributes: '
          '\nName: {} '
          '\nNumber: {} '
          '\nAnnual salary: {} '
          '\nYearly bonus: {}'.format(super.get_emp_name(), super.get_emp_num(),
                                       super.get_annual_salary(), super.get_yearly_bonus()))

main()

