#We used open in read mode and file.read to read and print to display.
file = open("testfile.txt","r")

first_line=file.readline()
print(first_line)
second_line=file.readlines()
print(second_line)

file.close()