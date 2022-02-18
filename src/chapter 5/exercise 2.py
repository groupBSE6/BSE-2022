maximum = 0
minimum = 0
while True:
    num = input("Enter a number: ").lower()
    if num == "done":
        break
    try:
        num = int(num)
        if num > maximum:
            maximum = num
        if minimum == 0:
            minimum = num
        else:
            if minimum > num:
               minimum =  num
    except:
        print("invalid input")

print(f"The maximum number is {maximum}\nThe minimum number is {minimum} ")

