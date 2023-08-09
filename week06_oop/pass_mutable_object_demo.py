from tv import TV

# Print channel inside the function
def print_channel(tv, ch):
    tv.set_channel(ch)
    print('Inside the function: Channel is', tv.get_channel())

# Create a default TV object
my_tv = TV()

# Print channel via the function
print_channel(my_tv, 8)

# Display my_tv.channel
print('After the function call: Channel is', my_tv.get_channel())
