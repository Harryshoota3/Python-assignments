'''
Now You Code 4: Email Harvesting Training

Description

Write a program to extract the email addresses from the mailbox
file "NYC4-mbox-short.txt" and save them into another file
"NYC4-emails.txt" with one extracted email address per line.

The best way to find the emails in the mailbox file is to search
for lines in the file that begin with "From:". When you find an email
write just the address (not "From:" and the address) to
"NYC4-emails.txt", and don't worry about duplicates.

The program should print the number of emails it wrote to the file.

Example Run:

Wrote 27 emails to NYC4-emails.txt


Start out your program by writing your TODO list of steps
you'll need to solve the problem!
'''

# TODO: Write Todo list then beneath write your code

# Write code here 

def copy_email(copyFileName,desFile):
    read_file = open(copyFileName,'r')
    content = read_file.read()
    words = content.split()
	    number_of_email = 0
    for x in words:
        if x == "From":
		            number_of_email = number_of_email + 1
            write_file = open(desFile, 'w')
            email = words[words.index(x)+1]
            write_file.write(email + "\n")
    print("The number of email is : ")
    print(number_of_email)    
copy_email("NYC4-mBox-short.txt","NYC4-emails.txt")