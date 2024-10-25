"""
Ms. Pan
10/25/24
Intensive Data Science 2
Classwork #7 - Lists

Indexing, slicing, appending
"""

import random

# Example 1: List indexing and slicing
shopping_list = ["milk", "eggs", "apples", "bagels"]

print(len(shopping_list))  # Print the length of the list

print(shopping_list[1])    # This prints: eggs
print(shopping_list[0])    # This prints: milk
print(shopping_list[-1])   # This prints: bagels
print(shopping_list[-2])   # This prints: apples
print(shopping_list[0:2])  # This prints: ["milk", "eggs"]

print()

# Example 2: Simulating n (1000) rolls and storing in a list
n = 1000
rolls = []

for i in range(n):
    roll = random.randint(1,6)  # Roll a die
    rolls.append(roll)                # Adds roll to the end of the list

total = sum(rolls)
avg = total / len(rolls)
print(f"total of {n} rolls: {total}")
print(f"average of {n} rolls: {avg}")
