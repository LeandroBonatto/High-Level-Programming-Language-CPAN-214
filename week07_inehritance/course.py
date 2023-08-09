class Course:
    def __init__(self, course_name):
        self.__course_name = course_name
        self.__students = []

    def add_student(self, student):
        self.__students.append(student)

    def get_students(self):
        return self.__students

    def get_number_of_students(self):
        return len(self.__students)

    def get_course_name(self):
        return self.__course_name

    def drop_student(self, student):
        self.__students.remove(student)
