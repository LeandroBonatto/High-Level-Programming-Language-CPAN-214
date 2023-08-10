filename = str(input("Enter a filename: ").strip())
be_replaced = input("Enter the existing string to be replaced: ").lower()
new_string = str(input("Enter the new string to replace the existing string: ")).lower()

inputFile = open(filename, "w")
inputFile.read(str(be_replaced))
inputFile.write(str(new_string))
inputFile = inputFile.replace(be_replaced, new_string)
inputFile.close()
print("done")



