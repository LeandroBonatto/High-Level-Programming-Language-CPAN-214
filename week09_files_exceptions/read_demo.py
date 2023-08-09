# Open file for input
input_file = open("Presidents.txt", "r")
print("(1) Using read(): ")
print(input_file.read())  # Read all in the file
input_file.close()  # Close the input file

# Open file for input
input_file = open("Presidents.txt", "r")
print("\n(2) Using read(number): ")
s1 = input_file.read(4)
print(s1)
s2 = input_file.read(15)  # Read 15 characters to s2
print(repr(s2))  # repr(object) Return a string containing a printable representation of an object.
print(s2)
input_file.close()  # Close the input file

# Open file for input
input_file = open("Presidents.txt", "r")
print("\n(3) Using readline(): ")
line1 = input_file.readline()  # Read a line
line2 = input_file.readline()
line3 = input_file.readline()
line4 = input_file.readline()
print(repr(line1))
print(repr(line2))
print(repr(line3))
print(repr(line4))
input_file.close()  # Close the input file

# Open file for input
input_file = open("Presidents.txt", "r")
print("\n(4) Using readlines(): ")
lines = input_file.readlines()
print(lines)
input_file.close()  # Close the input file

print('>>> END <<<')
