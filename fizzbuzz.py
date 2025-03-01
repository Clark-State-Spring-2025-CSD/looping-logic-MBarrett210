#Create a program that will run through the integers 1 to 25.
#If the number is a multiple of 3, print "Fizz"
#If the number is a multiple of 5, print "Buzz"
#If the number is a multiple of 3 and 5 print "FizzBuzz"
#If the number is not any of the stated multiples, print the number.
#Each output is on it's own line
#Also include in your repo a .drawio file that flowcharts out the logic

#Here is a section of sample output:
#Buzz
#11
#Fizz
#13
#14
#FizzBuzz

import random

random.seed()

enterNumber = int(input("Please Enter Number: "))

result = 0
FizzBuzz = 0

for i in range(enterNumber):
    result = random.randint(0,25)
    if result == enterNumber * 3:
        print ("Fizz")
    elif result == enterNumber * 5:
        print ("Buzz")
    elif result == enterNumber * 3 and 5:
        print ("FizzBuzz")
    else:
        FizzBuzz +=1

print (f"{result}")