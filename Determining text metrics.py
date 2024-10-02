# This code opens a file that the user inputs and then rcounts the 
# It also has exception handling if the user inputs an invalid file name 
words=0
characters=0
space=0


try:
    text_file=input("Enter a filename: ")
    my_file=open(text_file,"r") 
    lines=my_file.readlines()    #readlines reads all the lines, readline reads just the first line
    my_file.close()
except FileNotFoundError:
    print("This code was not executed as the file was not found")
else:   
    total_number_lines=len(lines)
    for line in lines:
            line_words=len(line.split())
            words+=line_words
            characters+=len(line)
            space+=line.count(" ")

    characters=characters-space
    print("The file has {} lines".format(total_number_lines))
    print("The file has {} words".format(words))
    print("The file has {} characters".format(characters))


