import random

def randInt(min=0, max=100):
    range_is = max - min
    return round(random.random() * range_is + min)     # this line grabs all possible print scenarios through each loop.
print(randInt())      # output between 0 to 100
print(randInt(max=50))      # output between 0 to 50
print(randInt(min=50)) # output between 50 to 100
print(randInt(min=50, max=500))  # output between 50 and 500