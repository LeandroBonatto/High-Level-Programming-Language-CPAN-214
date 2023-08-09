# Open file for writing binary
import pickle

outputFile = open("numbers.dat", "wb")

data = int(input("Enter an integer (the input exits " +
                 "if the input is 0): "))
while data != 0:
    pickle.dump(data, outputFile)
    data = int(input("Enter an integer (the input exits " +
                     "if the input is 0): "))

outputFile.close()  # Close the output file

# Open file for reading binary
inputFile = open("numbers.dat", "rb")

end_of_file = False
while not end_of_file:
    try:
        print(pickle.load(inputFile), end=" ")
    except EOFError:  # Catch eof error
        end_of_file = True

inputFile.close()  # Close the input file

print("\nAll objects are read")

print('\n>>> END <<<')
