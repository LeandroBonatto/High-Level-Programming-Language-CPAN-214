# Open file for writing binary
import pickle

outputFile = open("pickle.dat", "wb")
pickle.dump(45, outputFile)
pickle.dump(56.6, outputFile)  # Write a float 56.6
pickle.dump("Programming is fun", outputFile)
pickle.dump([1, 2, 3, 4], outputFile)
outputFile.close()  # Close the output file

# Open file for reading binary
inputFile = open("pickle.dat", "rb")
print(pickle.load(inputFile))  # Read an input
print(pickle.load(inputFile))
print(pickle.load(inputFile))
print(pickle.load(inputFile))
# print(pickle.load(inputFile))
inputFile.close()  # Close the input file

print('>>> END <<<')
