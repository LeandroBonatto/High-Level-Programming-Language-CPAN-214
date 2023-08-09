# Open file for output
output_file = open("Presidents.txt", "w")

# Write data to the file
output_file.write("George Washington\n")
output_file.write("John Adams\n")
output_file.write("Thomas Jefferson")  # Write Thomas Jefferson

output_file.close()  # Close the output file

import os.path

if os.path.isfile("Presidents.txt"):
    print("Presidents.txt is a file")

if os.path.isdir("Presidents.txt"):
    print("Presidents.txt is a directory")

print('>>> END <<<')
