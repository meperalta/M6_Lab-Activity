#Maria Eden Peralta
#February 27, 2022

#Problem 1:
#Use a for statement and random.randrange to print 10 random integers between 25 and 35.

import random

for i in range(10):
    print(random.randrange(25,35))

#Problem 2:
#Use random.randrange to print an odd integer between 0 and 100.

import random

print(random.randrange(0,100)*2+1)

#Problem 3:
#Use random.choice to select a day of the week from a list and print that day.

import random

days =["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]
print(random.choice(days))

#Problem 4:
#Search on the internet for a way to calculate an approximation for pi.
#There are many that use simple arithmetic. Write a program to compute the approximation
#and then print that value as well as the value of math.pi from the math module.

# Python Code to estimate value using Leibniz’s formula
# Import math Library
import math
# Initialize denominator
k = 1
# Initialize sum
s = 0
for i in range(1000000):
# even index elements are positive
    if i % 2 == 0:
        s += 4/k
    else:
# odd index elements are negative
        s -= 4/k
# denominator is odd
    k += 2

print('Value of estimated pi: ' , s)

# Print the value of pi
print('Value of pi from math module: ',math.pi)

#Problem 5:
#Search the internet for how to convert radians to degrees. Write a program to compute the conversion given a user input value.
#Print this value as well as the calculated value using the degrees function in the math module.

import math
print(math.radians(120))

#convert radians to degrees
import math
radians = 1.5707963267948966
radians = math.degrees(radians)
print(radians)

#Problem 6:
#Use a for statement to calculate the factorial of a user input value.
#Print this value as well as the calculated value using the factorial function in the math module.

import math

n = int(input('Enter an integer:'))
result = 1
for i in range(1, n+1):
    result = result * i
print('factorial of {} using for loop:{}'.format(n, result))
print('factorial of {} using inbuilt function:{}'.format(n, math.factorial(n)))








