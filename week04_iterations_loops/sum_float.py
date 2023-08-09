# Initialize sum
sum_of_floats = 0

# Add 0.01, 0.02, ..., 0.99, 1 to sum
i = 0.01
while i <= 1.0:
    sum_of_floats += i
    i = i + 0.01


# Display result
print("The sum is", sum_of_floats)
