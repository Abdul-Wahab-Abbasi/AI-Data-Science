# 1. What is File Handling in Python?

# File handling means working with files such as:

# .txt → text files
# .csv → spreadsheet-style data
# .json → structured data
# .log → logs/history

# Using Python, you can:

# Create files
# Read files
# Write new data
# Update existing data
# Delete files
# Store records permanently


# 2. Opening a File
# Python uses open().
# file = open("data.txt", "r") # open(filename, mode)
# to read content python uses read()
# print(file.read())


# 3. File Modes
# Mode	Meaning
# "r"	Read file
# "w"	Write (overwrite)
# "a"	Append (add at end)
# "x"	Create new file
# "rb"	Read binary
# "wb"	Write binary


# 4. Best Practice: Use "with open()"
# This auto-closes the file.
# with open("data.txt", "r") as file:
    # content = file.read()
    # print(content)

# Much better than:
# file = open("data.txt", "r")
# print(file.read())
# file.close()


# 5. Reading Files
# Read Full File
# with open("data.txt", "r") as file:
#     print(file.read())

# Read One Line
# with open("data.txt", "r") as file:
#     print(file.readline())

# Read All Lines
# with open("data.txt", "r") as file:
#     lines = file.readlines()
#     print(lines)


# 6. Writing Files
# Write New Data
# with open("data.txt", "w") as file:
#     file.write("Hello")

# ⚠️ Old content gets deleted.

# Append Data
# with open("data.txt", "a") as file:
#     file.write("\nNew Line Added")


# 7. Example: Save Student Data
# name = input("Enter name: ")
# age = input("Enter age: ")

# with open("students.txt", "a") as file: # notice we are using "a" mode so our previous data remain save
#     file.write(name + "," + age + "\n")

# 8. Reading Structured Records
# with open("students.txt", "r") as file:
#     for line in file:
#         name, age = line.strip().split(",")
#         print("Name:", name)
#         print("Age:", age)


# 9. Updating a Record
# Files cannot directly edit middle text easily. Common method:
# Read old data → modify → rewrite
# with open("students.txt", "r") as file:
#     lines = file.readlines()

# with open("students.txt", "w") as file:
#     for line in lines:
#         name, age = line.strip().split(",")

#         if name == "ali":
#             file.write("ali ahmed,25\n")
#         else:
#             file.write(line)

# 10. Delete File
# import os
# os.remove("students.txt")

# if os.path.exists("students.txt"):
#     os.remove("students.txt")
# else:
#     print("File not found")