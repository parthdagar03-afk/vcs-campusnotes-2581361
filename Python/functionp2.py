def calculate_discount(price, discount=10):
    final_price = price - (price * discount / 100)
    return final_price

print("With default discount:", calculate_discount(1000))
print("With custom discount:", calculate_discount(1000,20))