'''# import the whole module // first way
import module_example

module_example.demo("Parul")
result = module_example.add(3, 5)
print(result)


# second way
from module_example import * 

demo("Parul")
result = add(3, 5)
print("RESULT===== ",result)
'''
# import specific functions or variables from a module
from module_example import demo, add

demo("Parul")
result = add(10, 15)
print('Costom Function',result)


# Renaming a module 
import module_example as mm

mm.demo("Welcome")
result = mm.add(7, 8)
print(result)





