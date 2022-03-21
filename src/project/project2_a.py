try:
    file_name = open("measles.txt")
except:
    print("Un-able to open the file")
    exit

file_name = open("measles.txt")
output_file = input("Enter the output file : ")
year = input("Enter the year : ")


with open(output_file, "w") as file:
    for lines in file_name:

        if year.lower() == "all" or year == "": #All, all, "Empty Input"
            file.writelines(lines)
        elif int(year) == int(lines[88:]):# year
            file.writelines(lines)
        elif int(year) == int(lines[88]):
            file.writelines(lines)
        elif int(year) == int(lines[88:90]):
            file.writelines(lines)
        elif int(year) == int(lines[88:91]):
            file.writelines(lines)
#