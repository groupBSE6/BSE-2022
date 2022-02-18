sum = 0
count = 0
while True:
    num = input("enter the number: ").lower()
    try:
        if num == "done":
            break
        sum += int(num)
        count += 1
    except:
        print("invalid input")
average = (sum/count)
print(count, sum,average)
