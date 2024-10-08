"""
Ms. Pan
9/16/24
Intensive Data Science 2
Classwork #2 - Math in Python

Exploring the math module and calculating coin flip probabilities.
"""

import math

"""
print(math.pi)
print(math.sin(math.pi))

print(math.degrees(math.pi))
print(math.radians(180))
"""

n = int(input("Number of coin flips? "))
k = int(input("Number of heads? "))

prob = math.comb(n,k) / 2**n

percent = round(prob*100, 1)
print("The probability is: " + str(percent) + "%")
