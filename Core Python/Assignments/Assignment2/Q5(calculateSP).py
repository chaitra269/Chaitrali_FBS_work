# WAP to calculate selling price of book based on cost price and discount 
# start 
# enter cost price and discount 
cost_price = float(input("Enter cost price :"))
discount = float(input("Enter discount(%) :"))
dis_amount = (cost_price * discount) / 100
selling_price = cost_price - dis_amount
print(f"selling price = {selling_price}.")