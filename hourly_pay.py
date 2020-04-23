hrs = int(input("Enter Hours:"))
rate = float(input("Enter Rate:"))
if hrs > 40 :
    regular_hours = hrs * rate
    over_time = (hrs - 40.0) * (rate * 0.5)
    pay = regular_hours + over_time
elif hrs <= 40 :
    pay = hrs * rate
print(pay)