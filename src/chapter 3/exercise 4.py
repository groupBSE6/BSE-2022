try:
    age = int(input("Enter age:"))
    if age >= 18:
       print("you can vote")
    elif 0 < age <=17:
        print("Too young to vote")
    else:
         print("your a time traveller")
except:
       print("Enter a numeric input")