# Count each letter in the string
def count_letters(line, counts_dict):
    for ch in line:
        if ch.isalpha():  # Test if ch is a letter
            if ch not in counts_dict:
                counts_dict[ch] = 1
            else:
                counts_dict[ch] += 1


filename = input("Enter a filename: ").strip()
inputFile = open(filename, "r")  # Open the file

counts_dict = {}  # Create and initialize counts
for line in inputFile:
    # Invoke the count_letters function to count each letter
    count_letters(line.lower(), counts_dict)

# Display results
myKeys = list(counts_dict.keys())
myKeys.sort()
sorted_dict = {i: counts_dict[i] for i in myKeys}
for key in sorted_dict:
    print(key + " appears " + str(sorted_dict[key])
          + (" time" if sorted_dict[key] == 1 else " times"))

inputFile.close()  # Close file

print('>>> END <<<')
