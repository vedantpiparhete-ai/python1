def bill(u):
    if u<=100:
        return u*5
    elif u<=200:
        return (u-100)*7 + 100 * 5
    elif u<=300:
        return (u-200)*10 + 100 * 7 + 100 * 5


unit=int(input("Enter your unit consumption: "))
bill=bill(unit)
print(f"Total Bill: {bill}")