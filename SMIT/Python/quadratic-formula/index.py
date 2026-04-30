import math
a = float(input("Enter the coefficient a: "))
b = float(input("Enter the coefficient b: "))
c = float(input("Enter the coefficient c: "))
positiveSide = (-b + (b**2 - 4*a*c)**1/2)/2*a
negativeSide = (-b - (b**2 - 4*a*c)**1/2)/2*a
print(f"Root 1: {positiveSide}")
print(f"Root 2: {negativeSide}")