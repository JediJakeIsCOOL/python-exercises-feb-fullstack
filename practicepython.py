# a = [1, 1 ,2 ,3 ,5, 8 ,13 , 21, 34, 55 ,64]
# b = []
# for x in a:
#     if x < 5:
#         b.append(x)
    
        
#         print(b)

# userinp = int(input("what is the number?"))
# divlist = []
# for x in range(1, userinp):
#     if userinp % x == 0:
#         divlist.append(x)
#         print(divlist)

# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

# c= []
# for x in a:
#     for y in b:
#         if x == y:
#             c.append(x)
#             print(c)

# userinp = input("Is this a palindrome?")

# if userinp[:] == userinp[::-1]:
#     print("this is a palindrome")
# else:
#     print("this is not a palindrome")
# a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# b = []
# for x in a:
#     if x % 2 == 0:
#         b.append(x)
#         print(b)

# import random
# number = random.randint(1, 10)

# while True:
#     userinp = int(input("Guess a number 1 through 9"))
#     if userinp == number:
#         print("you got it")
#         break
#     if userinp < number:
#         print("guess higher")
#     if userinp > number:
#         print("guess lower")

import random

randlist = random.sample(range(1,30), 10)
print(randlist)