# This code runs in a text file of numbers, determines how many numbers, their total and their average. 
total_numbers=0
number_count=0
try:
    text_file=input("Enter a filename: ")
    my_file=open(text_file,"r") 
    lines=my_file.readlines()    #readlines reads all the lines, readline reads just the first line
    my_file.close()
except FileNotFoundError:
    print("This code was not executed as the file was not found")
else:   
    for line in lines:
            array_line=line.split()
            array_line=[int(m) for m in array_line]
            number_count+=len(array_line)
            total_numbers+=sum(array_line)
    average_number=round(total_numbers/number_count,1)

    print("There are {} numbers".format(number_count))
    print("The total is {}".format(total_numbers))
    print("The average number is {}".format(average_number))


