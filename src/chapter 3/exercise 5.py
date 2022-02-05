try:
    prompt = int(input("Enter the number of people that attend the wedding:"))
    if prompt <= 50:
       print("it must cost $4000")
    elif prompt <= 100:
        print("it must cost $10000")
    elif prompt <= 200:
        print("it must cost $15000")
    else:
         print("it must cost $20000")
except:
        print("WRONG INPUT:")