'''
#1
for num in range(1,11):
    print(num)
'''
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
for i in range(0,6):
    for j in range(0,6):
        print("*",end="")
    print("")