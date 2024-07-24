class Apple:
    def __init__(self):
        self.color = "red"
        self.flavor = "sweet"

honeycrisp = Apple()
print(honeycrisp.color)
# prints "red"

class Apple:
    def __init__(self, color, flavor):
        self.color = color
        self.flavor = flavor

honeycrisp = Apple("red", "sweet")
fuji = Apple("red", "tart")
print(honeycrisp.flavor)
print(fuji.flavor)
# prints "sweet" and "tart"

'''
dunder method
    __str__ 
    __len__ 
    __contains__ 
    __eq__ 
'''

class Apple:
    def __init__(self, color, flavor):
        self.color = color
        self.flavor = flavor

    # This method allows us to define how an instance of an object will be printed when it’s passed to the print() function.
    def __str__(self):
        return "an apple which is {} and {}".format(self.color, self.flavor)

honeycrisp = Apple("red", "sweet")
print(honeycrisp)
# prints "an apple which is red and sweet"


class Piglet:
    # the speak method is accessing the attribute name (instance variable) of the current instance of the Piglet class.
    name = "piglet"
    def speak(self):
        print("Oink! I'm {}!".format(self.name))

hamlet = Piglet()
hamlet.speak()

hamlet.name = "hamlet"
hamlet.speak()

petunia = Piglet()
petunia.name = "Petunia"
petunia.speak()

class Piglet:
    years = 0
    def pig_years(self):
        return self.years * 18
    
piggy = Piglet()
print(piggy.pig_years())

piggy.years = 2
print(piggy.pig_years())

'''
    Dunder methods to override standard operations
    https://docs.python.org/3/library/operator.html#mapping-operators-to-functions
'''

class Triangle:
    """This method is the constructor of the class."""
    def __init__(self, base, height):
        self.base = base
        self.height = height
    """This method calculate a tringle's area"""
    def area(self):
        return 0.5 * self.base * self.height
    """This method overrides the + operator to "add" two triangles together."""
    def __add__(self, other):
        return self.area() + other.area()
    
triangle1 = Triangle(10, 5)
triangle2 = Triangle(6, 8)
print("The area of triangle 1 is", triangle1.area())
print("The area of triangle 2 is", triangle2.area())
print("The area of both triangles is", triangle1 + triangle2)

print(triangle2.__doc__)
print(Triangle.__doc__)
print(triangle2.area().__doc__)
#help(Triangle)


