'''
#1
lista = [1, 2 ,3 ,4 ,5 ,6]
print(sum(lista))


#2 
listLg = [1, 4, 11, 23]
print(max(listLg))

#3
print(min(listLg))

#4 -
listFour = [1, 4, 11, 23, 12]
for num in listFour:
    if num % 2 == 0:
        print(num)

#5
listnegpos = [-1, -3 , 1 , 3 , 4]
for num in listnegpos:
    if num < 0:
        print(num)

#6
listNew =[]
listnegpos = [-1, -3 , 1 , 3 , 4]
for num in listnegpos:
    if num > 0:
        listNew.append(num)
print(listNew)
#7
listMult = [1, 2 ,3 ,4 ,5]
listNew = listMult * 2
print(listNew)

#8
list1 = [1, 3 , 4]
list2 = [5, 6 ,7]
newlist = []
for i in range(0,3):
    newlist.append(list1[i] * list2[i])
print(newlist)
'''
#9
x = [[2, -2],
     [5, 3]]
y = [[3, 3],
     [2, 4]]

z = [[0, 0],
    [0, 0]]

for i in range(len(x)):
   for j in range(len(x[0])):
  #    z[i][j] = x[i][j] + y[i][j]#
#for r in z:#
    print(i,j)
#10
'''
#11
list3 = [1, 3 , 4, 5 , 3 , 4 ,5 , 7 ,8 ]

newlist2 = set(list3)
print(list(newlist2))
'''