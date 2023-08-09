# Count each letter in the string
def count_letters(line, counts):
    for ch in line:
        if ch.isalpha():  # Test if ch is a letter
            counts[ord(ch) - ord('a')] += 1


filename = input("Enter a filename: ").strip()
inputFile = open(filename, "r")  # Open the file

counts = 26 * [0]  # Create and initialize counts
for line in inputFile:
    # Invoke the count_letters function to count each letter
    count_letters(line.lower(), counts)

# Display results
for i in range(len(counts)):
    if counts[i] != 0:
        print(chr(ord('a') + i) + " appears " + str(counts[i])
              + (" time" if counts[i] == 1 else " times"))

inputFile.close()  # Close file

print('>>> END <<<')
