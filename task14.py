limit = float(input('Enter total data limit: '))
used = float(input('Enter used data: '))
if used >= 0.9 * limit:
    print("Alert: Data limit almost reached")
else:
    print('Data used is normal')