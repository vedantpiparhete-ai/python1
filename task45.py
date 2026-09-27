t1 = [15000, 18000, 17000, 16000]
total = sum(t1)  # without libraray function -- sum = 0  : for e in n1 : sum = sum + n1
average = total/len(t1)
print('Total Sale: ',total)
print('Average Sale: ',average)
if total >= 100000:
    print('Target Achieved')
else:
    print('Target Not Achieved')