amount = float(input('Enter total amount : '))
if amount >= 5000:
    discount = amount * 0.10
else:
    discount = 0
finalamount = amount - discount

print('Discount Applied : ',discount)
print('Final Amount : ',finalamount)