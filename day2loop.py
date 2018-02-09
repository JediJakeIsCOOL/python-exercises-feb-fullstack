'''
#1
for num in range(1,11):
    print(num)

#2
start = input("starts on which number?")
end = input("Ends on which number?")
for num in range(int(start), int(end)+1):
    print(num)

#3
for num in range(1,11):
    if num % 2 != 0:
        print(num)
#4
'''
for i in range(0,6):
    for j in range(0,6):
        print("*",end="")
    print("")
'''
#5 
width1 = int(input("Width? "))


for j in range(width1):
    print("*" * width1)


#6
width = int(input('Width? '))
height = int(input('Height?' ))

print('*' * width)

for n in range(height - 2):
    print("*" + " " * (width - 2) + "*")


print('*' * width)



   *
  ***
 *****
*******

#7
space = 3
star = 1

for i in range(0,4):
    for j in range(0,space):
        print(" ", end = "")
    for k in range(0,star):
        print("*", end="")
    print("")
    space=space -1
    star = star +2

       *
      ***
     *****
    *******
   *********
  ***********
 *************

#8
user = int(input("how tall is the triangle?"))
space = user
star = 1

for i in range(0,user):
    for j in range(0,space):
        print(" ",end="")
    for k in range(0,star):
        print("*",end="")
    print("")
    space=space -1
    star = star +2
'''
#9 
for i in range(1,11):
    for j in range(1,11):
        print(i ,"X", j ,"=", i*j)