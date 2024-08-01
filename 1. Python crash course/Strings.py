name = "Nico"
color = "green"
print("Name: " + name, ", Favorite color: " + color)

#Repeat string
print(color * 4)

print(len(name))

#Print specific characters by using string indexing
text = "Random string with a lot of characters"
print(text[1])
print(text[-1])
print(text[-2])

#Print range of characterss by using string slicing
print(text[1:4])
print(text[:4])
print(text[4:])

message = "A kong string with a silly typo"

#message[2] = "l"
#This will throw an error as strings are immutable

new_message = message[0:2] + "l" + message[3:]
print(new_message)

pets="Cats & Dogs"
pets.index("&")
pets.index("C")
pets.index("Dog")
pets.index("s")

#pets.index("XX")
#This will throw an error: substring not found

pets="Cats & Dogs"
#pets.index("x")
#This will throw an error

#Instead, you can use the in keyword first, it will return true or false
"Dragons" in pets
"Cats" in pets


def replace_domain(email, old_domain, new_domain):
  if "@" + old_domain in email:
    index = email.index("@" + old_domain)
    new_email = email[:index] + "@" + new_domain
    return new_email
  return email

print(replace_domain("nicolas.jarma@chubb.com", "chubb.com", "outlook.es"))

#upper and lower
"Mountains".upper()
"Mountains".lower()

answer = "YES"
if answer.lower() == "yes":
  print("User said yes")

#Get rid of whitespace characters, similar to Trim() in C#
" yes ".strip()
" yes ".lstrip()
" yes ".rstrip()

#Count ocurrences
"The number of times e occurs in this string is 4".count("e")

"Forest".endswith("rest")
"Forest".startswith("yeah")

"Forest".isnumeric()
"12345".isnumeric()
print("xyzzy".isalpha())

print(int("12345") + int("54321"))

" ".join(["This", "is", "a", "phrase", "joined", "by", "spaces"])
"...".join(["This", "is", "a", "phrase", "joined", "by", "triple", "dots"])

"This is another example".split()

test = "How-much-wood-would-a-woodchuck-chuck"
print(test.split("-"))
print(test.replace("wood", "plastic"))

'''
Formatting strings
'''

name = "Manny"
number = len(name) * 3
print("Hello {}, your lucky number is {}".format(name, number))
print("Your lucky number is {number}, {name}.".format(name=name, number=len(name)*4))

price = 7.5
with_tax = price * 1.09
print(price, with_tax)
print("Base price: ${:.2f}. With Tax: ${:.2f}".format(price, with_tax))


def to_celsius(x):
  return (x-32)*5/9

for x in range(0,101,10):
  print("{:>3} F | {:>6.2f} C".format(x, to_celsius(x)))

for line in [[1, 128, 1298039], [123388, 0, 2]]:
    print('{:>8} {:>8} {:>8}'.format(*line))

print('{quantity} {item} cost ${price}'.format(
    quantity=6,
    item='bananas',
    price=1.74))


'''
    Formatting strings reference guide
'''

# Here are the items in the customer's basket. Each item is a tuple
# of (item name, weight, price per pound).
#
basket = [
    ("Peaches", 3.0, 2.99),
    ("Pears", 5.0, 1.66),
    ("Plums", 2.5, 3.99)
]


# Calculate the total price for each item (weight times price per pound)
# and add them up to get a subtotal.
#
subtotal = 0.00
for item in basket:
    fruit, weight, unit_price = item
    subtotal += (weight * unit_price)


# Now calculate the sales tax and total bill.
#
tax_rate = 0.06625 # 6.625% sales tax in New Jersey
tax_amt = subtotal * tax_rate
total = subtotal + tax_amt


# Print the receipt for the customer.
#
print("{text:<12}| {:>8.2f}".format(subtotal, text="Subtotal:"))
print("{text:<12}| {:>8.2f}".format(tax_amt, text="Salex Tax:"))
print("{text:<12}| {:>8.2f}".format(total, text="Total:"))


print("Subtotal:    ${:10,.2f}".format(subtotal))
print("Sales Tax:   ${:10,.2f}".format(tax_amt))
print("Total:       ${:10,.2f}".format(total))

# Using indexes
fruit = "peaches"
weight = 3.0
per_pound = 2.99

output = "{1} are {2} per pound, and you have {0} pounds of {1}.".format(weight, fruit, per_pound)
print(output)

# All the formatting expressions:
# https://docs.python.org/3/library/string.html#format-specification-mini-language

#Palindrome function
def is_palindrome(input_string):
    # Two variables are initialized as string date types using empty 
    # quotes: "reverse_string" to hold the "input_string" in reverse
    # order and "new_string" to hold the "input_string" minus the 
    # spaces between words, if any are found.
    new_string = ""
    reverse_string = ""

    # Complete the for loop to iterate through each letter of the
    # "input_string"
    for letter in input_string:

        # The if-statement checks if the "letter" is not a space.
        if letter != " ":

            # If True, add the "letter" to the end of "new_string" and
            # to the front of "reverse_string". If False (if a space
            # is detected), no action is needed. Exit the if-block.
            new_string = new_string + letter
            reverse_string = letter + reverse_string

    # Complete the if-statement to compare the "new_string" to the
    # "reverse_string". Remember that Python is case-sensitive when
    # creating the string comparison code. 
    if new_string.lower() == reverse_string.lower():

        # If True, the "input_string" contains a palindrome.
        return True
		
    # Otherwise, return False.
    return False

print(is_palindrome("Never Odd or Even")) # Should be True
print(is_palindrome("abc")) # Should be False
print(is_palindrome("kayak")) # Should be True



def convert_distance(miles):
    km = miles * 1.6 
    result = "{} miles equals {:.1f} km".format(miles, km)
    return result

print(convert_distance(12)) # Should be: 12 miles equals 19.2 km
print(convert_distance(5.5)) # Should be: 5.5 miles equals 8.8 km
print(convert_distance(11)) # Should be: 11 miles equals 17.6 km



def replace_ending(sentence, old, new):
    # Check if the old substring is at the end of the sentence 
    if sentence.endswith(old):
        # Using i as the slicing index, combine the part
        # of the sentence up to the matched string at the 
        # end with the new string
        i = sentence.rfind(old)
        new_sentence = sentence[:i] + new
        return new_sentence


    # Return the original sentence if there is no match 
    return sentence
    
print(replace_ending("It's raining cats and cats", "cats", "dogs")) 
# Should display "It's raining cats and dogs"
print(replace_ending("She sells seashells by the seashore", "seashells", "donuts")) 
# Should display "She sells seashells by the seashore"
print(replace_ending("The weather is nice in May", "may", "april")) 
# Should display "The weather is nice in May"
print(replace_ending("The weather is nice in May", "May", "April")) 
# Should display "The weather is nice in April"
