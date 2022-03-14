sum = 0
count = 0
file_name = input("enter a file name: ")
with open (file_name) as readfile:
    for line in readfile:
        line.upper()
        if line.startswith("X-DSPAM-Confidence"):
            var = line.find(":")
            var1 = float(line[19:])
            sum += (var1)
            count += 1
average = sum/count
print(f"average X-DSPAM-Confidence:{average}")
print(average)
print('aver xdc:',average)