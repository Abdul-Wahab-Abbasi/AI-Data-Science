# loops in python
# Loops are used to execute a block of code repeatedly until a certain condition is met.
# There are two types of loops in python: for loop and while loop.

# 1. for loop is used to iterate over a sequence (like list, tuple, string) or other iterable objects 
# basically we use for loop when we know the number of iterations.
# for loop
for i in range(5):
    print(f"Iteration {i}")

# for loop with list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(f"Fruit: {fruit}")

# for loop with string
name = "Python"
for letter in name:
    print(f"Letter: {letter}")

# for loop with enumerate
for index, fruit in enumerate(fruits):
    print(f"Index: {index}, Fruit: {fruit}")

# 2. while loop is used to execute a block of code repeatedly until a certain condition is met.
# basically we use while loop when we don't know the number of iterations.
# while loop
count = 0
while count < 5:
    print(f"Count: {count}")
    count += 1

# while loop with break and continue
# break statement is used to exit the loop when a certain condition is met.
# continue statement is used to skip the current iteration and move to the next iteration when a certain condition is met.
count = 0
while count < 10:
    if count == 5:
        print("Count is 5, breaking the loop.")
        break
    if count % 2 == 0:
        print(f"Count {count} is even, skipping.")
        count += 1
        continue
    print(f"Count: {count}")
    count += 1