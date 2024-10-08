"""
Ms. Pan
10/7/24
Intensive Data Science 2
Classwork #5 - Dice Roll Simulations

Simulating dice rolls to observe the law of large numbers.
The theoretical expected value of a 6-sided roll is 3.5.
"""

import random

# Exercise 1
total = 0
for i in range(1,11):
    roll = random.randint(1,6)
    total += roll
    #print(roll)
print(f"The sum of 10 rolls is: {total}")
print(f"The mean of 10 rolls is: {total/10}")

print("-----")

# Exercise 2
total = 0
for i in range(1, 100001):
    roll = random.randint(1,6)
    total += roll
    if i == 1:
        print(f"The average of 1 roll is: {total/i}")
    elif i == 10:
        print(f"The average of 10 rolls is: {total/i}")
    elif i == 100:
        print(f"The average of 100 rolls is: {total/i}")
    elif i == 1000:
        print(f"The average of 1000 rolls is: {total/i}")
    elif i == 10000:
        print(f"The average of 10000 rolls is: {total/i}")
print(f"The average of {i} rolls is: {total/i}")
print("Can you see the law of large numbers at play?")
