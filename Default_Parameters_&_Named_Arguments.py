import random

def Integer(min=0, max=100):
    range_is = max - min
    return round(random.random() * range_is + min)     # this line grabs all possible print scenarios through each loop.
print(Integer())      # output between 0 to 100
print(Integer(max=50))      # output between 0 to 50
print(Integer(min=50)) # output between 50 to 100
print(Integer(min=50, max=500))  # output between 50 and 500
