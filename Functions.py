#Calculate area of a triangle
base = 6
height = 3
area = (base * height) / 2
print(area)


#Create a function to calculate the area
def area_triangle(base:int, height: int):
    return (base*height)/2

base_a = 5
height_a = 4
area_a = area_triangle(base_a, height_a)
print("The area of the triangle with base {} and height {} is: {}".format(base_a, height_a, area_a))

base_b = 7
height_b = 3
area_b = area_triangle(base_b, height_b)
print("The area of the triangle with base {} and height {} is: {}".format(base_b, height_b, area_b))

sum = area_a + area_b

print("The sum of both areas is:", str(sum))
print(type(sum))

'''
Convert seconds in a touple with the following format:
    hours, minutes, seconds
'''
def convert_seconds(seconds: int):
    hours = seconds // 3600
    minutes = (seconds - hours * 3600) // 60
    remaining_seconds = seconds - hours * 3600 - minutes * 60
    return hours, minutes, remaining_seconds

seconds = 8400
print("The converstion for {} seconds is the following: {}".format(seconds, convert_seconds(seconds)))
print(type(convert_seconds(seconds)))


# This function calculates the number of days in a variable number of 
# years, months, and days. These variables are provided by the user and
# are passed to the function through the function’s parameters.
def find_total_days(years, months, days):
# Assign a variable to hold the calculations for the number of days in
# a year (years*365) plus the number of days in a month (months*30) plus
# the number of days provided through the "days" parameter variable.
    my_days = (years*365) + (months*30) + days
# Use the "return" keyword to send the result of the "my_days"  
# calculation to the function call. 
    return my_days
 
# Function call with user provided parameter values. 
print(find_total_days(2,5,23))


# This function converts fluid ounces to milliliters and returns the 
# result of the conversion.
def convert_volume(fluid_ounce):
# Calculate value of the "ml" variable using the parameter variable 
# "fluid_ounce". There are approximately 29.5 milliliters in 1 fluid
# ounce.
    ml = fluid_ounce * 29.5  
# Return the result of the calculation.  
    return ml
 
# Call the conversion from within the print() function using 2 fluid 
# ounces. Convert the return value from a float to a string.  
print("The volume in milliliters is " + str(convert_volume(2)))
 
# Call the function again and double the 2 fluid ounces from within
# the print function.
print("The volume in milliliters is " + str(convert_volume(2)*2))
# Alternative calculation:
# print("The volume in milliliters is " + str(convert_volume(4))


# 1) Complete the code to return the result of the conversion
def convert_distance(km):
	m = km * 1000  # exactly 1000 meters in 1 kilometer
	return m

# Do not indent any of the following lines of code as they are
# meant to be located outside of the function above
my_trip_kilometers = 55

# 2) Convert my_trip_kilometers to meters by calling the function above
my_trip_meters = convert_distance(my_trip_kilometers)

# 3) Fill in the blank to print the result of converting my_trip_kilometers
print("The distance in meters is " + str(my_trip_meters))



def print_seconds(hours, minutes, seconds):
   print(hours*3600+minutes*60+seconds)

print_seconds(1,2,3)
#output will print to the screen
