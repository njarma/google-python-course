'''
    While loop
'''
x =   0
while x < 5:
    print("Not there yet, x=" + str(x))
    x = x + 1
print("x=" + str(x))


def attempts(n):
    x = 1
    while x <= n:
        print("Attempt " + str(x))
        x += 1
    print("Done")

attempts(5)

#you can use functions to evaluate the while loop
'''
username = get_username()
while not valid_username(username):
    print("Invalid username")
    username = get_username()
'''
#This code will give an error because get_username is not defined

# Calculate the sum and product
x = 1
sum = 0
while x < 10:
    sum = sum + x
    x = x + 1

x = 1 #need to initialize again
product = 1
while x < 10:
    product = product * x
    x = x + 1

print(sum, product)
#Ouput 45 1

#How to solve infinite loops
while x % 2 == 0:
    x = x / 2
#No output

if x != 0:
    while x % 2 == 0:
        x = x / 2
#No output

x = 24
while x != 0 and x % 2 == 0:
    x = x / 2
    print(x)
#No output

'''
while True:
    do_something_cool()
    if user_requested_to_stop():
        break
'''
#This code will give an error because do_something_cool is not defined

'''
    Coding skills
'''

# Skill group 1

# This function counts the number of integer factors for a 
# "given_number" variable, passed through the function’s parameters.
# The "count" return value includes the "given_number" itself as a 
# factor (n*1). 
def count_factors(given_number):

    # To include the "given_number" variable as a "factor", initialize
    # the "factor" variable with the value 1 (if the "factor" variable
    # were to start at 2, the "given_number" itself would be excluded). 
    factor = 1
    count = 1

    # This "if" block will run if the "given_number" equals 0.
    if given_number == 0:
        # If True, the return value will be 0 factors. 
        return 0

    # The while loop will run while the "factor" is still less than
    # the "given_number" variable.
    while factor < given_number:
        # This "if" block checks if the "given_number" can be divided by
        # the "factor" variable without leaving a remainder. The modulo
        # operator % is used to test for a remainder.
        if given_number % factor == 0:
            # If True, then the "factor" variable is added to the count of
            # the "given_number"’s integer factors.
            count += 1
        # When exiting the if block, increment the "factor" variable by 1
        # to divide the "given_number" variable by a new "factor" value
        # inside the while loop.
        factor += 1

    # When the interpreter exits either the while loop or the top if
    # block, it will return the value of the "count" variable.
    return count


print(count_factors(0)) # Count value should be 0
print(count_factors(3)) # Should count 2 factors (1x3)
print(count_factors(10)) # Should count 4 factors (1x10, 2x5)
print(count_factors(24)) # Should count 8 factors (1x24, 2x12, 3x8, and 4x6). 

# Skill group 2

# This function outputs an addition table. It is written to end after
# printing 5 lines of the addition table, but it will break out of the
# loop if the "my_sum" variable exceeds 20.

# The function accepts a "given_number" variable through its
# parameters.
def addition_table(given_number):

	# The "iterated_number" and "my_sum" variables are initialized with
	# the value of 1. Although the "my_sum" variable does not need any
	# specific initial value, it still must be assigned a data type
	# before being used in the while loop. By initializing "my_sum"
	# with any integer, the data type will be set to int.
	iterated_number = 1
	my_sum = 1

	# The while loop will run while it is True that the
	# "iterated_number" is less than or equal to 5.
	while iterated_number <= 5:

		# The "my_sum" variable is assigned the value of the
		# "given_number" plus the "iterated_number" variables.
		my_sum = given_number + iterated_number

		# Test to see if the "my_sum" variable is greater than 20.
		if my_sum > 20:
			# If True, then use the break keyword to exit the loop.
			break

		# If False, the Python interpreter will move to the next line
		# in the while loop after the if-statement has ended.

		# The print function will output the "given_number" plus
		# the "iterated_number" equals "my_sum".
		print(str(given_number), "+", str(iterated_number), "=", str(my_sum))

		# Increment the "iterated_number" before the while loop starts
		# over again to print a new "my_sum" value.
		iterated_number += 1


addition_table(5)
addition_table(17)
addition_table(30)

# Expected output:
# 5 + 1 = 6
# 5 + 2 = 7
# 5 + 3 = 8
# 5 + 4 = 9
# 5 + 5 = 10
# 17 + 1 = 18
# 17 + 2 = 19
# 17 + 3 = 20
# None


def is_power_of_two(number):
  # This while loop checks if the "number" can be divided by two
  # without leaving a remainder. How can you change the while loop to
  # avoid a Python ZeroDivisionError?
  
  while number % 2 == 0:
    number = number / 2
    # this check is crutial to avoid infinite loop
    if number == 0:
      break
  # If after dividing by 2 "number" equals 1, then "number" is a power
  # of 2.
  if number == 1:
    return True
  return False
  
# Calls to the function
print(is_power_of_two(0)) # Should be False
print(is_power_of_two(1)) # Should be True
print(is_power_of_two(8)) # Should be True
print(is_power_of_two(9)) # Should be False


'''
    For loop
'''

for x in range(5):
    print(x)

# iterating strings
friends = ['Taylor', 'Alex', 'Pat', 'Eli']
for friend in friends:
    print("Hi " + friend)

#iterating integers
values = [ 23, 52, 59, 37, 48 ]
sum = 0
length = 0
for value in values:
    sum += value
    length += 1

print("Total sum: " + str(sum) + " - Average: " + str(sum/length))


# start the range with 1
product = 1
for n in range(1,10):
  product = product * n

print(product)

# increase the range by 10
def to_celsius(x):
  return (x-32)*5/9

for x in range(0,101,10):
  print(x, to_celsius(x))

'''
    Range function
'''

for n in range(1, 5, 6):  
    print(n)


# This loop iterates on the value of the "n" variable in a range
# of 0 to 10 (the value of the end-of-range index 11 is excluded).
# The incremental value for the loop is 2. The print() function will 
# output the resulting value of "n" as the loop counts from 0 to 10 
# (end-of-range index 11) in incremental steps of 2. This is one 
# method that can be used in Python to print a list of even numbers.

for n in range(0,11,2):
    print(n)
# The loop should print 0, 2, 4, 6, 8, 10


# This loop iterates on the value of the "number" variable in a range
# of 2 to 7+1 (the value of the end-of-range index 7 is excluded, so 
# +1 has been added to the parameter to include the numeric value 7 in 
# the range). The incremental value for the loop is the default of +1.
# The print() function will output the resulting value of "number" 
# multiplied by 3.

for number in range(2,7+1):
    print(number*3)
# The loop should print 6, 9, 12, 15, 18, 21


# This loop iterates on the value of the "x" variable in a range
# of 2 to -1 (the end-of-range index -2 is excluded). The third 
# parameter is also a negative number, making it a decremental value
# of -1. The print() function will output the resulting value of
# "x" as it starts at 2 and counts down to -1 (index -2).

for x in range(2, -2, -1):
    print(x)
# The loop should print 2, 1, 0, -1


# Nested for loops
for left in range(7):
  for right in range(left, 7):
    print("[" + str(left) + "|" + str(right) + "]", end=" ")
  print()

# Looping strings
greeting = "Hello"
for c in greeting:
    print("The next character is: ", c)

greeting = 'Hello'
for i in range(len(greeting)):
	print(i)

greeting = 'Hello'
index = 0
while index < len(greeting):
	print(greeting[index])
	index += 1

greeting = 'Hello'
index = 0
while index < len(greeting):
    print(greeting[index:index+1])
    index += 1

# List comprehension
numbers = [1, 2, 3, 4, 5]
squared_numbers = [x ** 2 for x in numbers]
print(squared_numbers)


fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if x != "apple"]
print(newlist)


fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x if x != "banana" else "orange" for x in fruits]
print(newlist)

'''
    Slice and Join Strings
'''

string1 = "Greetings, Earthlings"
print(string1[0])   # Prints “G”
print(string1[4:8]) # Prints “ting”
print(string1[11:]) # Prints “Earthlings”
print(string1[:5])  # Prints “Greet”
print(string1[-10:]) # Prints “Earthlings” again
print(string1[55:]) # Prints “”

'''
    How to join strings 
'''

print("Hello" + " " + "world") #Prints “Hello world”


greetings = ["Hello", "world"]
print(" ".join(greetings)) # Prints "Hello world"
#You can also concatenate a combination of strings and variables like in the following example.
name = "Alice"
print("Hello, " + name + "!") # Prints "Hello, Alice!"

'''
    How to combine slicing and joining strings
'''

phonenum = '2025551212'

# The first 3 digits are the area code:
area_code = "(" + phonenum[:3] + ")"
print("The area code is:", area_code)

# The next 3 digits are called the “exchange”:
exchange = phonenum[3:6]
print("The exchange is:", exchange)

# The next 3 digits are the line number:
line = phonenum[-4:]
print("The line number is:", line)

def format_phone(phonenum):
    area_code = "(" + phonenum[:3] + ")"
    exchange = phonenum[3:6]
    line = phonenum[-4:]
    return area_code + " " + exchange + "-" + line

print(format_phone("2025551212")) # Outputs: (202) 555-1212

'''
    List comprehension
'''

sequence = range(10)
new_list = []
for x in sequence:
    if x % 2 == 0:
        new_list.append(x)
print(new_list)

# Use this instead, using list comprehension.
sequence = range(10)
new_list = [x for x in sequence if x % 2 == 0]
print(new_list)

'''
    One liners
'''

print("*" * 8)
# prints: ********