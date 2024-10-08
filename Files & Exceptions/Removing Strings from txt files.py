# This code opens a file that the user inputs and then removes a specified word.
# It also has exception handling if the user inputs an invalid file name 
try:
    text_file=input("Enter a filename")
    my_file=open(text_file,"r") 
    lines=my_file.readlines()    #readlines reads all the lines, readline reads just the first line
    my_file.close()
except FileNotFoundError:
    print("Please check the filename is correct")
else:
    string_remove=input("Enter a string to be removed: ")
    new_list=[]
    for line in lines:
        if string_remove in line:
            line=line.replace(string_remove, "")
        new_list.append(line)    #append means add to the end of a list
    
    new_file=open(text_file, "w")
    for line in new_list:
        new_file.write(line)
    new_file.close


