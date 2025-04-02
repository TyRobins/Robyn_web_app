# Imports below:
import random

# Create lists below:
faces_d4 = list(range(1, 5))
faces_d6 = list(range(1, 7))
faces_d8 = list(range(1, 9))
faces_d10 = list(range(1, 11))
faces_d12 = list(range(1, 13))
faces_d20 = list(range(1, 21))

# Choose random numbers below:
randomer_d4 = random.choice(faces_d4)
randomer_d6 = random.choice(faces_d6)
randomer_d8 = random.choice(faces_d8)
randomer_d10 = random.choice(faces_d10)
randomer_d12 = random.choice(faces_d12)
randomer_d20 = random.choice(faces_d20)

# Create random numbers as functions below:
def randomer_fct_d4():
    return random.randint(1, 4)
def randomer_fct_d6():
    return random.randint(1, 6)
def randomer_fct_d8():
    return random.randint(1, 8)
def randomer_fct_d10():
    return random.randint(1, 10)
def randomer_fct_d12():
    return random.randint(1, 12)
def randomer_fct_d20():
    return random.randint(1, 20)