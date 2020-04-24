def computepay (h,r):

    if h > 40 :
    	regular_hours = h * r
    	over_time = (h - 40.0) * (r * 0.5)
    	pay = regular_hours + over_time
    elif h <= 40 :
    	pay = h * r
    return pay

hrs = int(input("Enter Hours:"))
rate = float(input("Enter Rate:"))
new_pay = computepay(hrs,rate)
print("Pay", new_pay)
