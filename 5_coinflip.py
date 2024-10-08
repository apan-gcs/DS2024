"""
Ms. Pan
9/24/24
Intensive Data Science 2
Classwork #3 - Coin Flip

We're gonna flip some coins today.
"""

import random

#random.seed(42)
#print(random.random())
#print(random.randint(1, 10))

print("Welcome to Double or Nothing!")

# Ask the user how many dollars they will bet
bet = int(input("How many dollars do you want to bet?: "))

# Simulate a coin flip
coin = random.randint(0, 1)

# If heads, win double
# if coin:
if coin == 1:
    print("Heads -- you win!")
    print(f"You now have: ${bet*2}")

# If tails, lose all money
else:
    print("Tails -- you lose!")
    print(f"You now have: $0")


# Extra Challenge: weighted coin, 40% / 60%
# coin = random.random()
# if coin < 0.4: print("Heads")
# else: print("Tails")
