try:
    text_file=input("Enter a filename: ")
    my_file=open(text_file,"r") 
    lines=my_file.readlines()    #readlines reads all the lines, readline reads just the first line
    my_file.close()
except FileNotFoundError:
    print("Please check the filename is correct")
else:
    new_list=[]
    string_remove=input("Enter the string to be replaced: ")
    new_string=input("Enter the new string to replace {}: ".format(string_remove))
    for line in lines:
        if string_remove in line:
            line=line.replace(string_remove, new_string)
        new_list.append(line)    #append means add to the end of a list
    
    new_file=open(text_file, "w")
    for line in new_list:
        new_file.write(line)
    new_file.close
