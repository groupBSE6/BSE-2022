prompt = int(input('enter an an amount to change for'))

twenties = (prompt // 20)
tennies = ((prompt % 20) // 10)
fives = (((prompt % 20) % 10) // 5)
ones = ((((prompt % 20) % 10) % 5) // 1)
cents = (((((prompt % 20) % 10) % 5) % 1) // 0.25)
dimes = ((((((prompt % 20) % 10) % 5) % 1) % 0.25) // 0.1)
nickel = (((((((prompt % 20) % 10) % 5) % 1) % 0.25) %  0.1)//0.05)
pennies = ((((((((prompt % 20) % 10) % 5) % 1) % 0.25) %  0.1) % 0.05) // 0.01)
print(f"{twenties} twenties \n .{tennies}  tennies \n{fives} f"
      f".2ives \n{ones} ones \n {cents} cents \n {dimes} dimes \n{nickel} nickel \n {pennies} pennies \n")