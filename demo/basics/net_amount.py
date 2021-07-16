# Calculation of net amount

price = int(input("Enter price :"))
qty = int(input("Enter qty : "))

amount = price * qty
discount = amount * 10 // 100  # 10% discount on amount
netamount = amount - discount

print("Net amount = ", netamount)
