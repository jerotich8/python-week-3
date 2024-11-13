def calculate_discount(price, discount_percentage):
    if discount_percentage >= 20:

        discount_amount = price * (discount_percentage / 100)

        final_price = price - discount_amount
        return final_price
    else:
        return price
    
# prompt user for input
price = float(input("Enter the actual price of the item:"))
discount_percentage = float(input("Enter the discount percentage:"))

final_price = calculate_discount(price, discount_percentage)

if final_price < price :
    print(f"The final price after {discount_percentage}%  discount is {final_price:.2f}")
else:
    print(f"No discount applied, The price is {price:.2f}")
