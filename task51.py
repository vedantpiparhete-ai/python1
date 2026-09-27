add=lambda m1,m2,m3,m4,m5:m1+m2+m3+m3+m5
per=lambda t:t/500*100
tot=add(85,90,80,85,95)
totper=per(tot)

def calgre(p):
    if p>=90:
        print("A Grade")
    elif p>=80:
        print("B Grade")
    elif p>=70:
        print("C Grade")
    else:
        print("fail")

print("Total marks you get: ",tot)
print("Total percentage you score: ",totper)