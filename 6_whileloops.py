"""
Ms. Pan
10/4/24
Intensive Data Science 2
Classwork #4 - While Loops

Two examples: factorial and prime number checker.
"""

# Factorial calculator - prints n!
n = 6
i = 1
result = 1

while i <= n:
    result = result * i
    #print(result)
    i += 1
print(f"{n}! = {result}")


# Prime number checker
number = 23
divisible = False
i = 2

while not divisible:
    print(i)
    if i >= number/2:
        print(f"{number} is prime.")
        break
    if number % i == 0:
        divisible = True
        print(f"{number} is not prime.")
    i = i + 1  # i += 1
