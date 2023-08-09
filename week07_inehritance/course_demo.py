from course import Course

def main():
    course1 = Course("Data Structures")
    course2 = Course("Database Systems")

    course1.add_student("Peter Jones")
    course1.add_student("Brian Smith")
    course1.add_student("Anne Kennedy")

    course2.add_student("Peter Jones")
    course2.add_student("Steve Smith")

    print("Number of students in course1:",
          course1.get_number_of_students())
    students = course1.get_students()
    for student in students:
        print(student, end=", ")

    course1.drop_student("Peter Jones")
    print("\nNumber of students in course1:",
          course1.get_number_of_students())
    students = course1.get_students()
    for student in students:
        print(student, end=", ")

    print("\nNumber of students in course2:",
          course2.get_number_of_students())

main()  # Call the main function
