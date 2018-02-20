"""#5 
work = [0, 1 , 2, 3, 4,]
sleep = [5 , 6]
userinp = input("what day of the week is it?")
if userinp in  range(0,5):
    print("go to work")
else:
    print("sleep in")

#6
temp = input("What is the temperature")
print(int(temp) * 1.8 + 32, "F")

#7

billAmt = input("How much was the bill")
service = input("How was the service, good, fair, or bad?")
if service == "good":
    print("Tip amount: ", "{:.2f}".format(0.20 * int(billAmt)))
    print("Total bill amount?", "{:.2f}".format(int(billAmt) + 0.2 * int(billAmt)) )
if service == "fair":
    print("Tip amount: ", "{:.2f}".format(0.15 * int(billAmt)))
    print("Total bill amount?", "{:.2f}".format(int(billAmt) + 0.15 * int(billAmt)) )
if service == "bad": 
    print("Tip amount: ", "{:.2f}".format(0.10 * int(billAmt)))
    print("Total bill amount?", "{:.2f}".format(int(billAmt) + 0.10 * int(billAmt)) )


#8
tip ={"good":.2, "fair":.15, "bad":.1}
billAmt = input("How much was the bill")
service = input("How was the service, good, fair, or bad?")
split = input("Split how many ways?")
total = int(billAmt) + tip[service] * int(billAmt)
if service == "good":
    print("Tip amount: ", "{:.2f}".format(0.20 * int(billAmt)))
    print("Total bill amount?", "{:.2f}".format(int(billAmt) + 0.2 * int(billAmt)) )
if service == "fair":
    print("Tip amount: ", "{:.2f}".format(0.15 * int(billAmt)))
    print("Total bill amount?", "{:.2f}".format(int(billAmt) + 0.15 * int(billAmt)) )
if service == "bad": 
    print("Tip amount: ", "{:.2f}".format(0.10 * int(billAmt)))
    print("Total bill amount?", "{:.2f}".format(int(billAmt) + 0.10 * int(billAmt)) )
print("split how many ways?", int(split))
print("Amount per person?", "{:.2f}".format(total / int(split)))


#9
count = 0
while count < 10:
  count += 1
  print(count)
"""
#10
coins = 0
while True:
    userinp = input("Do you want a coin?").upper()
    if userinp == "YES":
        coins = coins + 1
        print(coins)
    else:
        break
print("you have" ,coins, "coins")            

