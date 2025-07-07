# Write a program to create a text file and write some content to it.

file=open("testfile.txt","w")

file.write("Hello there this is my file that i have created\n")
file.writelines("my self kartikay\n"
"A computer science student\n"
"passing out in 2026\n")

file.close()
