# Prompt the user to enter the number of students
num_students = int(input("Enter the number of students: "))

# Ensure that there are two or more students
if num_students < 2:
  print("Error: The number of students must be at least 2.")
  exit()

# Initialize variables to keep track of the highest two scores and their corresponding names
first_name = ""
first_score = -1
second_name = ""
second_score = -1

# Loop through each student
for i in range(num_students):
  # Prompt the user to enter the student's name and score
  name = input("Enter the name of student {}: ".format(i + 1))
  score = int(input("Enter the score of student {}: ".format(i + 1)))

  # Update the first and second scores and names if necessary
  if score > first_score:
    second_name = first_name
    second_score = first_score
    first_name = name
    first_score = score
  elif score > second_score:
    second_name = name
    second_score = score

# Display the top two students
print("The top two students are:")
print("1. {} with a score of {}".format(first_name, first_score))
print("2. {} with a score of {}".format(second_name, second_score))
