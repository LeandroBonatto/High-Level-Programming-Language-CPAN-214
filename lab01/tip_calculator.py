subtotal, gratuity = eval(input("Enter the subtotal and gratuity rate? "))

gratuity = subtotal * (gratuity/100)
total = subtotal + gratuity

print('The gratuity is {:.2f}, and the total is {:.2f}'.format(subtotal, total))

# subtotal, tip_rate = eval(input("Enter the subtotal and gratuity rate? "))

# tip = subtotal + tip_rate / 100
# total = subtotal + tip

# print('The gratuity is ' + format(tip, ':.2f') + ', and the total is ' + format(total, ':.2f') + '.')
# print('The gratuity is {:.2f}, and the total is {:.2f}'.format(subtotal, total))
