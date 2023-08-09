# A stub for printMonth may look like this
def print_month(year, month):
    print("printMonth")


# A stub for printMonthTitle may look like this
def print_month_title(year, month):
    print("printMonthTitle")


# A stub for getMonthBody may look like this
def print_month_body(year, month):
    print("printMonthBody")


# A stub for getMonthName may look like this
def get_month_name(month):
    print("getMonthName")


# A stub for getStartDay may look like this
def get_start_day(year, month):
    print("getStartDay")


# A stub for getTotalNumberOfDays may look like this
def get_total_number_of_days(year, month):
    print("getTotalNumberOfDays")


# A stub for getNumberOfDaysInMonth may look like this
def get_number_of_days_in_month(year, month):
    print("getNumberOfDaysInMonth")


# A stub for isLeapYear may look like this
def is_leap_year(year):
    print("isLeapYear")


def main():
    # Prompt the user to enter year and month
    year = int(input("Enter full year (e.g., 2001): "))
    month = int(input((
        "Enter month as number between 1 and 12: ")))

    # Print calendar for the month of the year
    print_month(year, month)


main()
