unit = int(input('Enter units: '))
if unit <= 100:
    print('Category: Low Usage')
elif unit <= 200:
    print('Category: Medium Usage')
else:
    print('Category: High Usage')