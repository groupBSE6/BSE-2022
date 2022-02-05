Hours = (input("Enter your Hours: "))
try :
     int(Hours)
except :
    print("Error, input numerical values.")
    exit()

Rate = (input("Enter your rate: " ))
try :
    float(Rate)
except :
    print("Error, input numerical values.")
    exit()
Hours=int(Hours)
Rate=float(Rate)

if Hours > 40 :
    new = (Hours - 40)
    payone = new * (1.5 * Rate)
    pay = payone + (40 * Rate)
else :
    pay = Hours * Rate
print(pay)
