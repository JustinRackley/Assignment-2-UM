hrs = int(input("Enter Hours:"))
rate = float(input("Enter Rate:"))
if hrs > 40 :
    regular_hours = hrs * rate
    over_time = (hrs - 40.0) * (rate * 0.5)
    pay = regular_hours + over_time
    print(pay)
elif hrs <= 40 :
    no_overtime = hrs * rate
    print(no_overtime)