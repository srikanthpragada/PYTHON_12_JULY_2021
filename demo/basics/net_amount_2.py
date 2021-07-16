# Calculation of net amount

price = int(input("Enter price :"))
qty = int(input("Enter qty : "))

amount = price * qty
discount = amount * 10 // 100  # 10% discount on amount
grossamount = amount - discount
tax = grossamount * 8 // 100
netamount = grossamount + tax

print(f"Price              {price:8}")
print(f" * Qty             {qty:8}")
print(f"Amount             {amount:8}")
print(f" - Discount 10%    {discount:8}")
print(f"Discounted Amount  {grossamount:8}")
print(f" + Tax 8 %         {tax:8}")
print(f"Net amount         {netamount:8}")
