import os
# Reading the file
f=open("E:\File Handeling\sample.txt")
c=f.read()
print(c)

#creating new file
with open("sample2.txt", 'w') as file:
    file.write("rough")
d=open("sample2.txt")
print(d.read())

directory = "E:\File Handeling"

files = os.listdir(directory)
for file in files:
    print(file)
