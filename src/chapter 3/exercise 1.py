hours = int(input("Enter Hours:"))
rate = float(input("Enter rate: "))
if hours > 40:
   c = (hours- 40) * (15/10*rate)
   d = c + (40 * rate)
   print("PAY:",d)
else:
   print(hours*rate)