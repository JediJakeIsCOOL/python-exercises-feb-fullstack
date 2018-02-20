'''
file_handle = open('helloW.txt', 'w')
file_handle.write('Hello world\n')
file_handle.close()

file_handle = open('HelloW.txt','r')
contents = file_handle.read()
file_handle.close()
print(contents)

#1
userinp = input("what is the name of the file you want to open?")
file_name = open(userinp, 'r')
contents1 = file_name.read()
file_name.close()
print(contents1)
 #2
filename = input("What is the filename?")
file_contents = input("What are the files contents")
with open(filename, 'w') as file_name1:
    file_name1.write(file_contents)
'''
#3
filename1 = input("What is the file name ")

letterhis= {}
wordhis= {}

file_variable = open(filename1, "r")

readin = file_variable.read()

newreadin = readin.split()

for i in range(0, len(readin)):
    if readin[i] in letterhis:
        letterhis[readin[i]] +=  1
    else:
        letterhis[readin[i]] = 1



for i in range(0, len(newreadin)):
    if newreadin[i] in wordhis:
        wordhis[newreadin[i]] = wordhis[newreadin[i]] + 1
    else:
        wordhis[newreadin[i]] = 1


print(letterhis)

print(wordhis)


