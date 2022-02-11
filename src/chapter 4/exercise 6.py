def computepay(hours, rate):
    if hours > 40:
        extra = (hours - 40 ) * (rate * 1.5)
        pay = (40 * rate) + extra
        print("Pay : ",pay)
    else:
        pay = hours * rate
        print("Pay : ",pay)

hours = input("Enter Hours : ")
try:
    int(hours)
except:
    print("Enter Valid Input")
    exit()

rate = input("Enter Rate : ")
try:
    float(rate)
except:
    print("Enter valid Input")
    exit()

hours = int(hours)
rate = float(rate)

computepay(hours, rate)