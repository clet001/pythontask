'''Steps:

sum equals zero
product equls zero
counter equls one
average equals two

initiate while
cpllect input
use to get your smallest and largest'''

sum = 0
product = 0 
counter = 1
average = 2


while counter <= 4: 
    number = int(input("Enter first numb: "))
    sum = sum + number
    product = product * number
    average = number / average

if counter == 1:
    smallest = number
    largest = number

if number < smallest:
    print(number, "equals to smallest")

if number > largest:
   print(number, "equals to smallest")

counter = counter + 1



