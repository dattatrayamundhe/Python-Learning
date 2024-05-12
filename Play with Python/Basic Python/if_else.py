price = int(input("Enter the price of donuts: Rs."))
quantity = int(input("Enter the no. of quantity you want as N:"))
amount = price*quantity

if amount>1000 :
    print("Yeh..discount 10% is applicable")
    discount = amount*10/100
    amount = amount-discount
elif amount>500:
    print("Yeh..discount 5% is applicable")
    discount = amount*5/100
    amount = amount-discount
else:
    print("Discount is not applicable...")

print("The amount is payble Rs.",amount)


