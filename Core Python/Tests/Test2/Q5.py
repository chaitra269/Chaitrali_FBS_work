# A man goes for shopping. He buys 5 products. Accept the price of all products and display
# the total bill after adding 18% GST

# Program to generate shopping bill with GST
prices = []

# Accept prices for 5 products
for i in range(1, 6):
    price = float(input(f"Enter the price of product {i}: "))
    prices.append(price)

subtotal = sum(prices)
gst_amount = subtotal * 0.18
total_bill = subtotal + gst_amount

print("\n--- FINAL BILL ---")
print(f"Subtotal: Rs. {subtotal:.2f}")
print(f"GST (18%): Rs. {gst_amount:.2f}")
print(f"Total Amount to Pay: Rs. {total_bill:.2f}")
