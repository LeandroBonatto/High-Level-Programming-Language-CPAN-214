def compute_gratuity_and_total(subtotal, gratuity_rate):
    gratuity = subtotal * gratuity_rate / 100
    total = subtotal + gratuity
    return gratuity, total

subtotal = float(input("Enter the subtotal: "))
gratuity_rate = float(input("Enter the gratuity rate (%): "))

gratuity, total = compute_gratuity_and_total(subtotal, gratuity_rate)

print(f"Gratuity: ${gratuity:.2f}")
print(f"Total: ${total:.2f}")
