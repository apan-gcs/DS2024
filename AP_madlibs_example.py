"""
Ms. Pan
9/20/24
Intensive Data Science 2
Q1 Mini-Project: Mad Libs

An example story in which the user enters random words into a preset story.
Based on the CodeHS Mad Libs module.
"""

def indef_article(word):
    """Chooses the correct indefinite article (a or an)."""
    if word[0].lower() in ['a', 'e', 'i', 'o', 'u']:
        return 'an'
    else:
        return 'a'

print("Welcome to Mad Libs! Please enter the following words...")

word1 = input("A name: ")
word2 = input("A plural noun: ")
word3 = input("An adjective: ")
word4 = input("A noun: ")
word5 = input("A verb: ")
word6 = input("An adjective: ")

story = f"""One day, I went to the {word1}'s Corner Store to buy {word2}.
Unfortunately, they didn't have any, so I bought {indef_article(word3)} {word3} {word4} instead. 
The cashier told me to {word5} it as soon as I got home, so I did.
I had {indef_article(word6)} {word6} dinner that day."""

print(story)