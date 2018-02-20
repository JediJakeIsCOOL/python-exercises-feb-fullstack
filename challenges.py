
for number in range(1, 101):
    if number % 5 == 0 and number % 3 == 0:
         print("FizzBuzz")
    elif number % 3 == 0:
        #list1.append(number)
        print("Fizz")
    elif number % 5 == 0:
        #list2.append(number)
         print("Buzz")
    else:
        print(number)