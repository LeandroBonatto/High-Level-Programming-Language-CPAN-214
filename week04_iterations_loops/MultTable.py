# Set the table size
size = 10

# Print the header row
print("  ", end="")
for i in range(1, size+1):
    print("{:4d}".format(i), end="")
print()

# Print the table contents
for i in range(1, size+1):
    print("{:2d}".format(i), end="")
    for j in range(1, size+1):
        product = i * j
        print("{:4d}".format(product), end="")
    print()
