try:
    file_name = open("measles.txt")
except:
    print("Un-able to open the file")
    exit

file_name = open("measles.txt")
output_file = input("Enter the output file : ")
year = input("Enter the year : ")
with open(output_file, "w") as file:
    for line in file_name:
        if year.lower() == "all" or year == "": #All, all, "Empty Input"
            file.write(line)
        elif int(year) == int(line[88:]):# year
            file.write(line)
        elif int(year) == int(line[88]):
            file.write(line)
        elif int(year) == int(line[88:90]):
            file.write(line)
        elif int(year) == int(line[88:91]):
            file.write(line)
        