count = 0
file_name = input("enter a file name: ")
if file_name == "na na boo boo":
    print("na na boo boo".upper(),"you have been punk'd!")
    quit()
try:
    fhandle = open(file_name)
    for line in fhandle:
        if line.startswith("X-DSPAM-Confidence"):
            count += 1

except:

    print(f"File cannot be opened:{file_name}")
print(f"There were {count} subject lines in mbox.txt")
