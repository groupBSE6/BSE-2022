with open ("mbox-short.txt","r") as readfile:
    for line in readfile:
        print(line.upper().rstrip())
        