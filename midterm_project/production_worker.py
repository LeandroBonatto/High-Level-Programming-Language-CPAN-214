from company_people import Employee

class Production_Worker(Employee):
    def __init__(self, emp_name, emp_num, shift_worker, hr_pay_rate):
        super().__init__(emp_name, emp_num)
        self.__shift_worker = shift_worker
        self.__hr_pay_rate = hr_pay_rate

    def get_shift_worker(self):
        return self.__shift_worker

    def set_shift_worker(self, shift_worker):
        self.__shift_worker = shift_worker

    def get_hr_pay_rate(self):
        return self.__hr_pay_rate

    def set_hr_pay_rate(self, hr_pay_rate):
        self.__hr_pay_rate = hr_pay_rate

def main():
    prodworker = Production_Worker("", 0, 0, 0.00)
    prodworker.set_emp_name(input("Input employee name: "))
    prodworker.set_emp_num(int(input("Input employee number: ")))
    prodworker.set_shift_worker(int(input("Input number 1 for day shift or 2 for night shift: ")))
    prodworker.set_hr_pay_rate(float(input("Input pay rate: ")))

    #prodworker1 = Production_Worker(empName="", empNum=0, shiftWorker=0, hrPayRate=0.00 )
    #prodworker1.set_empName("")
    #prodworker1.set_empNum(0)
    #prodworker1.set_shiftWorker(0)
    #prodworker1.set_hrPayRate(0.00)

    print('Employee attributes: '
          '\nName: {} '
          '\nNumber: {} '
          '\nShift: {} '
          '\nPay rate/hr: {}'.format(prodworker.get_emp_name(), prodworker.get_emp_num(), prodworker.get_shift_worker(), prodworker.get_hr_pay_rate()))

main()