def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        final_price = price * (1 - discount_percent / 100)
        return final_price
    else:
        return price

# Prompt the user for input
price = float(input("Enter the original price of the item: "))
discount_percent = float(input("Enter the discount percentage (0-100): "))

# Calculate the final price
final_price = calculate_discount(price, discount_percent)

# Print the final price
if final_price == price:
    print("No discount was applied. The original price is: ", price)
else:
    print("The final price after applying the discount is: ", final_price)