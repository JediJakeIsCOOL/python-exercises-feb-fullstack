'''
def hello(name):
    return("Hello", {}.format(name))

#2

import matplotlib.pyplot as plot

def f(x):
    return x + 1

xs = list(range(-3, 4))
ys = []
for x in xs:
    ys.append(f(x))

plot.plot(xs, ys)
plot.show()


#3
import matplotlib.pyplot as plot

def f(x):
    return x * x

xs = list(range(-100, 101))
ys = []
for x in xs:
    ys.append(f(x))

plot.plot(xs, ys)
plot.show()

#4
import matplotlib.pyplot as plot

def f(x):
    while True:
        if x % 2 != 0:
            return 1
        if x % 2 == 0:
            return -1

xs = list(range(-5, 6))
ys = []
for x in xs:
    ys.append(f(x))

plot.bar(xs, ys)
plot.show()

#5
import matplotlib.pyplot as plot
import math
def f(x):
    return math.sin(x)

xs = list(range(-5, 6))
ys = []
for x in xs:
    ys.append(f(x))

plot.plot(xs, ys)
plot.show()

#6 
import matplotlib.pyplot as plot
from numpy import arange
import math
def f(x):
   return math.sin(x)

xs = list(arange(-5, 6, .1))
ys = []
for x in xs:
    ys.append(math.sin(x))

plot.plot(xs, ys)
plot.show()
'''
#8
import matplotlib.pyplot as plot
userinp = int(input("whats the temp in Celcius So I can convert to Fahrenheit? "))

def ass(x):
    F= userinp * 1.8 + 32
    return F
    

xs = list(range(0, 5))
ys = []
for x in xs:
    ys.append(ass(x))

plot.plot(xs, ys)
plot.show()
