def computegrade(score):
    if score >= 0.9:
        print("A")
    elif score >= 0.8:
        print("B")
    elif score >= 0.7:
        print("c") 
    elif score >= 0.6:
        print("D") 
    else:
        print("F")      

score = input("Enter the score : ")    
try:
    score = float(score)
    if score > 1 or score < 0:
        raise ValueError
except ValueError:
    print("Bad Score")
    exit()

score = float(score)
computegrade(score)
