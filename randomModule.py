import random

# random() funtion generate a randome number between 0 included and 1 excluded
print(random.random())

# generate random number between range
print(random.uniform(2,9))

# generate random integer between start and end
print(random.randint(6,100))

# chose random number from list
lst=[2,4,6,2,9,8]
print(random.choice(lst))

# generate n random number from list
print(random.sample(lst,4))