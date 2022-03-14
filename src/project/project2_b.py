def open_file():
    while True:
        input_file = input("Enter the file name : ")
        try:
            file_name = open(input_file, "r")
            break
        except FileNotFoundError:
            print("Un-able to open the file")
    return file_name

def process_file(file_object):
    Income_Level = ["WB_LI","WB_LMI","WB_UMI","WB_HI"]
    
    # Validating User input for the year
    while True:
        year = input("Enter the year : ")
        try:
            int(year)
            break
        except:
            print("Enter a valid year")
            continue

    # Validating user input for the income level (1, 2, 3, 4) - Expected Input
    while True:
        income_level_input = input("Enter the income level : ")
        try:
            income_level_input = int(income_level_input)
            # validate whether input is in the range 1 to 4
            if income_level_input >= 1 and income_level_input <= 4:
                break
        except:
            print("Enter Valid input")
            continue
    
    income_level_input = int(income_level_input)
    # End of data validation

    vaccinated_percentage = 0 
    highest_percentage = 0
    highest_country = ""
    lowest_percentage = 100
    lowest_country = ""
    count = 0
    sum = 0
    for lines in file_object:
        if int(year) == int(lines[88:]):
            if income_level_input == 1 and Income_Level[income_level_input-1] in lines: # Low Income
                vaccinated_percentage = int(lines[57:61])
                ### SUM
                sum = sum + vaccinated_percentage
                ### Highest and Lowest
                if vaccinated_percentage > highest_percentage:
                    highest_percentage = vaccinated_percentage
                    highest_country = lines[:50].rstrip()
                    
                if vaccinated_percentage <= lowest_percentage:
                    lowest_percentage = vaccinated_percentage
                    lowest_country = lines[:50].rstrip()
                ### Count
                count += 1
            elif income_level_input == 2 and Income_Level[income_level_input-1] in lines: # Low Income
                vaccinated_percentage = int(lines[57:61])
                ### SUM
                sum = sum + vaccinated_percentage
                ### Highest and Lowest
                if vaccinated_percentage > highest_percentage:
                    highest_percentage = vaccinated_percentage
                    highest_country = lines[:50].rstrip()
                    
                if vaccinated_percentage <= lowest_percentage:
                    lowest_percentage = vaccinated_percentage
                    lowest_country = lines[:50].rstrip()
                ### Count
                count += 1
            elif income_level_input == 3 and Income_Level[income_level_input-1] in lines: # Low Income
                vaccinated_percentage = int(lines[57:61])
                ### SUM
                sum = sum + vaccinated_percentage
                ### Highest and Lowest
                if vaccinated_percentage > highest_percentage:
                    highest_percentage = vaccinated_percentage
                    highest_country = lines[:50].rstrip()
                    
                if vaccinated_percentage <= lowest_percentage:
                    lowest_percentage = vaccinated_percentage
                    lowest_country = lines[:50].rstrip()
                ### Count
                count += 1
            elif income_level_input == 4 and Income_Level[income_level_input-1] in lines: # Low Income
                vaccinated_percentage = int(lines[57:61])
                ### SUM
                sum = sum + vaccinated_percentage
                ### Highest and Lowest
                if vaccinated_percentage > highest_percentage:
                    highest_percentage = vaccinated_percentage
                    highest_country = lines[:50].rstrip()
                    
                if vaccinated_percentage <= lowest_percentage:
                    lowest_percentage = vaccinated_percentage
                    lowest_country = lines[:50].rstrip()
                ### Count
                count += 1
    
        ################################
        elif int(year) == int(lines[88]):
            if income_level_input == 1 and Income_Level[income_level_input-1] in lines: # Low Income
                vaccinated_percentage = int(lines[57:61])
                ### SUM
                sum = sum + vaccinated_percentage
                ### Highest and Lowest
                if vaccinated_percentage > highest_percentage:
                    highest_percentage = vaccinated_percentage
                    highest_country = lines[:50].rstrip()
                    
                if vaccinated_percentage <= lowest_percentage:
                    lowest_percentage = vaccinated_percentage
                    lowest_country = lines[:50].rstrip()
                ### Count
                count += 1
            elif income_level_input == 2 and Income_Level[income_level_input-1] in lines: # Low Income
                vaccinated_percentage = int(lines[57:61])
                ### SUM
                sum = sum + vaccinated_percentage
                ### Highest and Lowest
                if vaccinated_percentage > highest_percentage:
                    highest_percentage = vaccinated_percentage
                    highest_country = lines[:50].rstrip()
                    
                if vaccinated_percentage <= lowest_percentage:
                    lowest_percentage = vaccinated_percentage
                    lowest_country = lines[:50].rstrip()
                ### Count
                count += 1
            elif income_level_input == 3 and Income_Level[income_level_input-1] in lines: # Low Income
                vaccinated_percentage = int(lines[57:61])
                ### SUM
                sum = sum + vaccinated_percentage
                ### Highest and Lowest
                if vaccinated_percentage > highest_percentage:
                    highest_percentage = vaccinated_percentage
                    highest_country = lines[:50].rstrip()
                    
                if vaccinated_percentage <= lowest_percentage:
                    lowest_percentage = vaccinated_percentage
                    lowest_country = lines[:50].rstrip()
                ### Count
                count += 1
            elif income_level_input == 4 and Income_Level[income_level_input-1] in lines: # Low Income
                vaccinated_percentage = int(lines[57:61])
                ### SUM
                sum = sum + vaccinated_percentage
                ### Highest and Lowest
                if vaccinated_percentage > highest_percentage:
                    highest_percentage = vaccinated_percentage
                    highest_country = lines[:50].rstrip()
                    
                if vaccinated_percentage <= lowest_percentage:
                    lowest_percentage = vaccinated_percentage
                    lowest_country = lines[:50].rstrip()
                ### Count
                count += 1

        ######################################
        elif int(year) == int(lines[88:90]):
            if income_level_input == 1 and Income_Level[income_level_input-1] in lines: # Low Income
                vaccinated_percentage = int(lines[57:61])
                ### SUM
                sum = sum + vaccinated_percentage
                ### Highest and Lowest
                if vaccinated_percentage > highest_percentage:
                    highest_percentage = vaccinated_percentage
                    highest_country = lines[:50].rstrip()
                    
                if vaccinated_percentage <= lowest_percentage:
                    lowest_percentage = vaccinated_percentage
                    lowest_country = lines[:50].rstrip()
                ### Count
                count += 1
            elif income_level_input == 2 and Income_Level[income_level_input-1] in lines: # Low Income
                vaccinated_percentage = int(lines[57:61])
                ### SUM
                sum = sum + vaccinated_percentage
                ### Highest and Lowest
                if vaccinated_percentage > highest_percentage:
                    highest_percentage = vaccinated_percentage
                    highest_country = lines[:50].rstrip()
                    
                if vaccinated_percentage <= lowest_percentage:
                    lowest_percentage = vaccinated_percentage
                    lowest_country = lines[:50].rstrip()
                ### Count
                count += 1
            elif income_level_input == 3 and Income_Level[income_level_input-1] in lines: # Low Income
                vaccinated_percentage = int(lines[57:61])
                ### SUM
                sum = sum + vaccinated_percentage
                ### Highest and Lowest
                if vaccinated_percentage > highest_percentage:
                    highest_percentage = vaccinated_percentage
                    highest_country = lines[:50].rstrip()
                    
                if vaccinated_percentage <= lowest_percentage:
                    lowest_percentage = vaccinated_percentage
                    lowest_country = lines[:50].rstrip()
                ### Count
                count += 1
            elif income_level_input == 4 and Income_Level[income_level_input-1] in lines: # Low Income
                vaccinated_percentage = int(lines[57:61])
                ### SUM
                sum = sum + vaccinated_percentage
                ### Highest and Lowest
                if vaccinated_percentage > highest_percentage:
                    highest_percentage = vaccinated_percentage
                    highest_country = lines[:50].rstrip()
                    
                if vaccinated_percentage <= lowest_percentage:
                    lowest_percentage = vaccinated_percentage
                    lowest_country = lines[:50].rstrip()
                ### Count
                count += 1

        #########################################
        elif int(year) == int(lines[88:91]):
            if income_level_input == 1 and Income_Level[income_level_input-1] in lines: # Low Income
                vaccinated_percentage = int(lines[57:61])
                ### SUM
                sum = sum + vaccinated_percentage
                ### Highest and Lowest
                if vaccinated_percentage > highest_percentage:
                    highest_percentage = vaccinated_percentage
                    highest_country = lines[:50].rstrip()
                    
                if vaccinated_percentage <= lowest_percentage:
                    lowest_percentage = vaccinated_percentage
                    lowest_country = lines[:50].rstrip()
                ### Count
                count += 1
            elif income_level_input == 2 and Income_Level[income_level_input-1] in lines: # Low Income
                vaccinated_percentage = int(lines[57:61])
                ### SUM
                sum = sum + vaccinated_percentage
                ### Highest and Lowest
                if vaccinated_percentage > highest_percentage:
                    highest_percentage = vaccinated_percentage
                    highest_country = lines[:50].rstrip()
                    
                if vaccinated_percentage <= lowest_percentage:
                    lowest_percentage = vaccinated_percentage
                    lowest_country = lines[:50].rstrip()
                ### Count
                count += 1
            elif income_level_input == 3 and Income_Level[income_level_input-1] in lines: # Low Income
                vaccinated_percentage = int(lines[57:61])
                ### SUM
                sum = sum + vaccinated_percentage
                ### Highest and Lowest
                if vaccinated_percentage > highest_percentage:
                    highest_percentage = vaccinated_percentage
                    highest_country = lines[:50].rstrip()
                    
                if vaccinated_percentage <= lowest_percentage:
                    lowest_percentage = vaccinated_percentage
                    lowest_country = lines[:50].rstrip()
                ### Count
                count += 1
            elif income_level_input == 4 and Income_Level[income_level_input-1] in lines: # Low Income
                vaccinated_percentage = int(lines[57:61])
                ### SUM
                sum = sum + vaccinated_percentage
                ### Highest and Lowest
                if vaccinated_percentage > highest_percentage:
                    highest_percentage = vaccinated_percentage
                    highest_country = lines[:50].rstrip()
                    
                if vaccinated_percentage <= lowest_percentage:
                    lowest_percentage = vaccinated_percentage
                    lowest_country = lines[:50].rstrip()
                ### Count
                count += 1

                ######################################################
    ### Average of the percentage
    Average = sum/count
    print(f"The count is {count}")
    print(f"The average percentage {Average}")
    print(f"{lowest_country} has the lowest percentage vacinnated with {lowest_percentage} %")
    print(f"{highest_country} has the highest percentage vacinnated with {highest_percentage} %")

def main():
    x = open_file()
    process_file(x)

main()