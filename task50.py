from datetime import datetime

now = datetime.now()

login_date = now.strftime("%d-%m-%Y")
login_time = now.strftime("%I:%M:%S %p")
day = now.strftime("%A")

print("Employee Attendance")
print("---------------------------")
print("Login Date :", login_date)
print("Login Time :", login_time)
print("Day        :", day)