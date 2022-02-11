def investment(C, r, n, t):
    p = (C*(1 + (r/n))**(t*n))
    p = round(p, 2)
    print("The final investment is, ", p)

C = input("Enter the initial Amount of Investment : ")
try:
    int(C)
except:
    print("invalid input") 
    exit()

r = input("Enter the yearly rate of Interest : ")
try:
    float(r)
except:
    print("invalid input")
    exit()

t = input("Enter number of years untill maturation : ")
try:
    int(t)
except:
    print("invalid input")
    exit()

n = input("Enter number of times the interest is compunded per year : ")
try:
    int(n)
except:
    print("invalid input")
    exit()

n = int(n) 
t = int(t)
C = int(C)
r = float(r)
investment(C, r, n, t)