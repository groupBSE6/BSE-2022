location = input("Enter your  location:")
pay = int(input("Enter pay:"))
location = location.upper()
try:

    if location == "mbarara" and pay > 4000000:
       print("without doubt l'll take  it")
    elif location == "kampala" and pay >= 10000000:
        print("without doubt l'll take  it")
    elif location == "space" and pay is not None:
         print("without doubt l'll take  it")
    elif location != "mbarara" and "kamapala" and pay >= 6000000:
          print("sure, i can work with this")
    else:
          print("No Thanks, can find something better")
except:
    print("No Thanks, can find something better")


