x = 40
y = 25
######################
# ARTHEMETIC OPERATORS
######################
print(x + y)  # Addition
print(x - y)  # Subtraction
print(x * y)  # Multiplication
print(x / y)  # Division (returns float)
print(x % y)  # Modulus (returns reminder of division)
print(x ** y) # Exponentiation 
print(x // y) # Floor Division (returns int part)

######################
# ASSIGNMENT OPERATORS
######################

# 1. =  → Assigns value on right to variable on left
z = 30
print(z)  # 30

# 2. += → Adds right value to variable and assigns result
z += 5
print(z)  # 35

# 3. -= → Subtracts right value from variable and assigns result
z -= 5
print(z)  # 30

# 4. *= → Multiplies variable by right value and assigns result
z *= 2
print(z)  # 60

# 5. /= → Divides variable by right value and assigns result (float)
z /= 5
print(z)  # 12.0

# 6. %= → Divides and keeps only the remainder
z %= 9
print(z)  # 3.0

# 7. //= → Floor divides (keeps only whole number part)
z //= 2
print(z)  # 1.0

# 8. **= → Raises variable to the power of right value
z = 2
z **= 2
print(z)  # 4

# 9. &= → Bitwise AND and assign (keeps bits that are 1 in both)
z = 2     # 10 (binary)
z &= 3    # 11 (binary)
print(z)  # 2

# 10. |= → Bitwise OR and assign (sets bits that are 1 in either)
z = 2     # 10
z |= 3    # 11
print(z)  # 3

# 11. ^= → Bitwise XOR and assign (sets bits that are different)
z = 2     # 10
z ^= 3    # 11
print(z)  # 1

# 12. >>= → Right shift and assign (moves bits right — divide by 2)
z = 8     # 1000
z >>= 2   # shift right 2 times
print(z)  # 2

# 13. <<= → Left shift and assign (moves bits left — multiply by 2)
z = 3     # 11
z <<= 2   # shift left 2 times
print(z)  # 12

# 14. := → Walrus operator (assigns value as part of an expression)
# Example: assign while checking condition
if (n := 5) > 3:
    print(n)  # 5

#######################
# Comparision OPERATORS
#######################
x = 2
y = 6
a = "SMIT"
b = "HYD"

# 1. ==
print(x == y)
# 2. !=
print(x != y)
# 3. >
print(x > y)
# 4. <
print(x < y)
# 5. >=
print(x >= y)
# 6. <=
print(x <= y)

# with string
# 1. ==
print(a == b)
# 2. !=
print(a != b)
# 3. >
print(a > b)
# 4. <
print(a < b)
# 5. >=
print(a >= b)
# 6. <=
print(a <= b)

#######################
# Logical OPERATORS
#######################
x = True
y = False

print(x and y)   # False: both must be True
print(x or y)    # True: at least one True
print(not x)     # False: negation
print(not y)     # True

# mixing with comparisons
a = 5
b = 10
print(a < b and b < 20)   # True
print(a > b or b < 20)    # True

#######################
# Identity OPERATORS
#######################
p = [1, 2, 3]
q = p
r = [1, 2, 3]

print(p is q)      # True: same object
print(p is r)      # False: different objects with same contents
print(p is not r)  # True

#######################
# Membership OPERATORS
#######################
s = "hello"
t = [1, 2, 3]

print('h' in s)       # True
print('z' not in s)   # True
print(2 in t)         # True
print(4 not in t)     # True