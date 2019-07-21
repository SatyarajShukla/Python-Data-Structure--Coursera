8.4 Open the file romeo.txt and read it line by line. For each line, split the line into a list of words using the split() method.
The program should build a list of words. For each word on each line check to see if the word is already in the list and 
if not append it to the list. When the program completes, sort and print the resulting words in alphabetical order. 
You can download the sample data at 
http://www.py4e.com/code3/romeo.txt 
Solution:
fname = input("Enter file name: ")
fh = open(fname)
lst = list()                       # list for the desired output
for line in fh:                    # to read every line of file romeo.txt
    word= line.rstrip().split()    # to eliminate the unwanted blanks and turn the line into a list of words
    for element in word:           # check every element in word    
        if element in lst:         # if element is repeated
            continue               # do nothing
        else :                     # else if element is not in the list
            lst.append(element)    # append     
lst.sort()                         # sort the list (de-indent indicates that you sort when the loop ends)
print (lst)                        # print the list

8.5 Open the file mbox-short.txt and read it line by line. When you find a line that starts with 'From ' like the following line: From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
You will parse the From line using split() and print out the second word in the line (i.e. the entire address of the person who sent the message). Then print out a count at the end. 
Hint: make sure not to include the lines that start with 'From:'.
You can download the sample data at  http://www.py4e.com/code3/mbox-short.txt 

Solution:
fname = input("Enter file name: ")
counter = 0
fh = open(fname)

for line in fh :
    line = line.rstrip()
    if not line.startswith('From '): continue        
    words = line.split()
    print(words[1])
    counter +=1
print ("There were", counter, "lines in the file with From as the first word")
