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