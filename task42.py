t1 = [32, 35, 38, 36, 33]
# sum = sum(m1) : sum
average = sum(t1)/len(t1)
print('Average Marks: ',average)
print('Marks above average: ')
for t1  in t1:
    if t1 > average:
        print(t1)