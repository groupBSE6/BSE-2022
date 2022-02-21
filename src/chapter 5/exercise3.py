
    #group 6
# - BWAMBALE EDGAR KAHERU
# -TENDO LAALA ANTONIA
# -OKEMA ELVIS ATUHAIRWE
# -NANTUMBWE PROSSY K
# -ATUSSASIRE BONITOR
# 21/2/2022

# Welcoming page to the vending machine
print("Welcome to the vending machine change maker program \nChange marker initialized")
# initiating variables for the dollars
nickels = 25
dimes = 25
quarters = 25
ones = 0
fives = 0

# list storing cents with their values
values = [0.05, 0.1, 0.25, 1, 5]
stock = [nickels, dimes, quarters, ones, fives]
currency = ["quarters", "dimes", "nickels"]

# logic for computing change
# using a while true loop
while True:
    print(f"Stock contains: \n\t{stock[0]} nickels \n\t{stock[1]} dimes \n\t{stock[2]} quarters \n\t{stock[3]} ones \n\t{stock[4]} fives")
    purchase_price =input("Enter the purchase  price (xx.xx) or 'q' to quit: ")
    if purchase_price == "q": # logic for computing quarters
        cents = nickels*5 + dimes*10 + quarters*25
        if cents >= 100:
            dollars = cents//100
            print(f" {dollars + ones*1 + fives*5} dollars and {cents - dollars*100} cents")
    else:
        if float(purchase_price) * 100 % 5 == 0:
            checked_balance = float(purchase_price)
            amount_paid = 0
            print(f"Menu for deposits: \n\t'n' - deposit a nickel \n\t'd' - deposit a dime \n\t'q' - deposit a quarter \n\t'o' - deposit a one dollar bill \n\t'f' - deposit a five dollar bill \n\t'c' - cancel the purchase")
            while checked_balance > 0:
                if checked_balance > 1:
                    print(f"Payment due: {int(checked_balance)} dollars and {int((abs(checked_balance) - (int(checked_balance))) * 100)} cents")
                else:
                    print(f"Payment due: {int((abs(checked_balance) - (int(checked_balance))) * 100)} cents")
                amount_deposited = input("Indicate your deposit: ")
                count = 0
                for i in "ndqof":
                    if amount_deposited == i:
                        checked_balance -= values[count]
                        stock[count] += 1
                        amount_paid += values[count]
                    count += 1
                if amount_deposited == "c":
                    checked_balance = -(amount_paid)
            if checked_balance < 0:
                count1 = 0 # initailizing count
                money_to_be_returned = round(abs(checked_balance), 2) * 100
                print("Please take the change below")
                if int(money_to_be_returned) == 0:
                    print("\nPlease take the change below")
                    print("No change due\n")
                while count1 < 3:
                    value_to_be_returned = money_to_be_returned//(values[2 - count1] * 100)
                    if stock[2 - count1] >= value_to_be_returned:
                        if int(value_to_be_returned) > 0:
                            print(int(value_to_be_returned), currency[count1])
                            money_to_be_returned -= int(value_to_be_returned) * (values[2 - count1]*100)
                            stock[2 - count1] -= int(value_to_be_returned)
                        count1 += 1
                    else:
                        if int(value_to_be_returned) > 0:
                            print(int(stock[2 - count1]), currency[count1])
                            money_to_be_returned -= stock[2 - count1] * (values[2 - count1]*100)
                            stock[2 - count1] -= stock[2 - count1]
                        count1 += 1
                # if money to be returned is not equal to 0
                if money_to_be_returned != 0:
                    if money_to_be_returned > 100:
                        print(f"Machine out of change \nSee store manager for remaining refund.\nAmount Due: {money_to_be_returned//100} dollars and {money_to_be_returned - ((money_to_be_returned//100) * 100)}")
                    else:
                        print(f"Machine out of change \nSee store manager for remaining refund.\nAmount Due: {round((money_to_be_returned))} cents")
