

# Modules allow you to organize code into logical groups, 
# making it easier to manage and reuse.
# Modules and packages in Python are essential for organizing code, 
# reusing functionality, and maintaining code modularity. 
# By leveraging both built-in and custom modules, 
# you can build complex and scalable applications efficiently.



# custome module example 
def demo(name):
    print("Hello",name)

def add(a, b):
    return a + b



# pre define modules for 2 mark
import datetime

current_date = datetime.date.today()
current_time = datetime.datetime.now().time()
print('DATE  : ', current_date)
print('TIME  : ', current_time)

# random module for 2 mark
import random

# Generates a random integer between 1 and 10 
random_number = random.randint(1, 10) 
print('RANDOM NUMBER :',random_number)

# Selects a random fruit from the list
fruits = ['apple', 'banana', 'orange', 'grapes', 'mango']
random_fruit = random.choice(fruits)  
print('RANDOM FRUITES :',random_fruit)

# random with dictionary
import random

my_dict = {'id': 1, 'name': 'charmi', 
           'age': 34, 'birth-date': '31st jan'}

# Convert the dictionary keys to a list and select a random key
random_key = random.choice(list(my_dict.keys()))
print("Random key:", random_key)


####  EXTRAA ####

#  Math Module
import math

print('Squer Root : ',math.sqrt(25))         # Square root
print('PI Value :', math.pi)               # Pi constant
 









