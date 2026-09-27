fare = float(input("Enter Fare: "))
time = float(input("Enter Time (Peak/Normal): "))
if time.lower() == "peak":
    fare = fare + 50
print("Final Fare: ",fare,"/-")