#######################
# Python List
#######################
thisList = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print("List: ", thisList)

# Some things you must know about list
#######################
# List Items
# List items are ordered, changeable, and allow duplicate values.

# List items are indexed, the first item has index [0], the second item has index [1] etc.

# Ordered
# When we say that lists are ordered, it means that the items have a defined order, and that order will not change.

# If you add new items to a list, the new items will be placed at the end of the list.

# Note: There are some list methods that will change the order, but in general: the order of the items will not change.

# Changeable
# The list is changeable, meaning that we can change, add, and remove items in a list after it has been created.

# Allow Duplicates
# Since lists are indexed, lists can have items with the same value

# Access Items
print(thisList[1]) # Print the second item of the list
print(thisList[-1]) # Print the last item of the list
print(thisList[2:5]) # return third, fourth and fifth item

print(thisList[:4]) # returns the items from the beginning to, but NOT including, "kiwi"
print(thisList[2:]) # returns the items from "cherry" to the end

# Change Item Value
thisList2 = ["apple", "banana", "cherry"]
print("Before change: ", thisList2)
thisList2[1] = "blackcurrant"
print("After change: ", thisList2)

thisList2[1:2] = ["blackcurrant", "watermelon"]
print(thisList2)

# Add List Items
thisList3 = ["apple", "banana", "cherry"]
thisList3.append("orange") # Using the append() method to append an item
print(thisList3)

thisList3.insert(1, "kiwi") # The insert() method inserts an item at the specified index
print(thisList3)

# Remove List Items
thisList3.remove("banana")
print(thisList3)
_list = ["apple", "banana", "cherry", "banana"] # here we have duplicate item "banana"
print(_list)
_list.remove("banana") # Remove the first occurrence of "banana"
print(_list)

thisList3.pop(1)
print(thisList3) # pop() method removes the specified index. 
thisList3.pop() # If you do not specify the index, the pop() method removes the last item.
print(thisList3)

thisList3 = ["apple", "banana", "cherry", "orange", "kiwi"]
del thisList3[0] # The del keyword also removes the specified index
print(thisList3)

del thisList3 # The del keyword can also delete the list completely.