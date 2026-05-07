# Functions in Python are self-contained, reusable blocks of code designed to
# perform a specific task. They help make code modular, reduce repetition
# (following the "DRY" or Don't Repeat Yourself principle), and improve
# maintainability.

# To define a function, use the def keyword followed by the function name,
# parentheses, and a colon.

# defining a function
def firstFunction():
    print("This is my first function python")
# calling a function
firstFunction()

def calcTemp(f):
    print((f - 32) * 5 / 9)

calcTemp(50)

# Functions can send data back to the code that called them using the return
# statement.

# When a function reaches a return statement, it stops executing and sends the
# result back:
# using return keyword
def calcTemp(f):
    return (f - 32) * 5 / 9

result = calcTemp(100)
print(result)


# Function definitions cannot be empty. If you need to create a function placeholder
# without any code, use the pass statement:
# using pass keyword
def emptyFunc():
    pass
# The pass statement is often used when developing, allowing you to define the
# structure first and implement details later.

# Parameters vs Arguments
# The terms parameter and argument can be used for the same thing: information that are passed into a function.

# From a function's perspective:

# A parameter is the variable listed inside the parentheses in the function definition.

# An argument is the actual value that is sent to the function when it is called.

def my_function(name): # name is a parameter
  print("Hello", name)

my_function("Emil") # "Emil" is an argument

# Default Parameter Values
# You can assign default values to parameters. If the function is called without an argument, it uses the default value:

def my_function(name = "friend"):
  print("Hello", name)

my_function("John")
my_function()

# Keyword Arguments
# You can send arguments with the key = value syntax.
def my_function(animal, name):
  print("I have a", animal)
  print("My", animal + "'s name is", name)
my_function(animal = "Cow", name = "Buddy")

# with keyword arguments, the order of the arguments does not matter.
my_function(name = "Buddy", animal = "Cow")

# Positional Arguments
# When you call a function with arguments without using keywords, they are called
# positional arguments.
# Positional arguments must be in the correct order:
def my_function(animal, name):
  print("I have a", animal)
  print("My", animal + "'s name is", name)

my_function("dog", "Buddy")
my_function("Buddy", "dog")


# Mixing Positional and Keyword Arguments
# You can mix positional and keyword arguments in a function call.
# However, positional arguments must come before keyword arguments

def my_function(region, animal, name, age):
  print("I have a", age, "year old", region, animal, "named", name)

my_function("german", "dog", name = "Buddy", age = 5)



# *args and **kwargs
# By default, a function must be called with the correct number of arguments.

# However, sometimes you may not know how many arguments that will be passed into
# your function.

# *args and **kwargs allow functions to accept a unknown number of arguments.

# Arbitrary Arguments - *args
# If you do not know how many arguments will be passed into your function, add a *
# before the parameter name.

# This way, the function will receive a tuple of arguments and can access the items
# accordingly:


# Using *args to accept any number of arguments:

def my_function(*kids):
  print("The youngest child is " + kids[2])
  print("All children " , kids)

my_function("Emil", "Tobias", "Linus")


# Using *args with Regular Arguments
# You can combine regular parameters with *args.
# Regular parameters must come before *args:
def my_function(greeting, *names):
  for name in names:
    print(greeting, name)

my_function("Hello", "Emil", "Tobias", "Linus")


# Arbitrary Keyword Arguments - **kwargs
# If you do not know how many keyword arguments will be passed into your function,
# add two asterisks ** before the parameter name.

# This way, the function will receive a dictionary of arguments and can access the
# items accordingly:
# Using **kwargs to accept any number of keyword arguments:

def my_function(**kid):
  print("His last name is " + kid["lname"])
  print("His first name is " + kid["fname"])

my_function(fname = "Tobias", lname = "Refsnes")


# Using **kwargs with Regular Arguments
# Regular parameters must come before **kwargs:
def my_function(username, **details):
  print("Username:", username)
  print("Additional details:")
  for key, value in details.items():
    print(" ", key + ":", value)

my_function("emil123", age = 25, city = "Oslo", hobby = "coding")

# Combining *args and **kwargs
# You can use both *args and **kwargs in the same function.

# The order must be:

# regular parameters
# *args
# **kwargs

