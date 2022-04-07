# Basic
for i in range(0, 151):
    print(i)


# Multiples of 5
print([i for i in range(5,1000,5)])


# Counting, the Dojo Way
def counting_dojo():
    for i in range (1,101,1):
        if i % 5 == 0:
            print ('Coding')
        if i % 10 == 0:
            print ('Dojo')
        if i > 0:
            print(i, end = ' ')

counting_dojo()


# Whoa. That Sucker's Huge
minimum = 0
maximum = 500000
Oddtotal = 0

for number in range(minimum, maximum+1):
    if(number % 2 != 0):
        print("{0}".format(number))
        Oddtotal = Oddtotal + number

print("The Sum of Odd Numbers from {0} to {1} = {2}".format(minimum, maximum, Oddtotal))


# Countdown by Fours
def count_down_four():
    number = 2018
    while number > 0:
        print (number)
        number = number - 4
        
count_down_four() 


# Flexible Counter
def flex_countdown(low, high, mult):
    for i in range (low, high):
        if i % mult == 0:
            print (i)
            
flex_countdown(2, 9, 3)