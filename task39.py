m1 = [45, 67, 89, 55, 72]
# sum = sum(m1) : sum
average = sum(m1)/len(m1)
print('Average Marks: ',average)
print('Marks above average: ')
for m1  in m1:
    if m1 > average:
        print(m1)