'''
Created on Oct 25, 2022

@author: agkri
'''
from laptop import *


Laptop = laptop("Dell", 10)
Laptop.setWeight(100)
print(Laptop)
print(Laptop.__repr__())
Laptop.getBrand()

'''
from laptop import *

laptop = object(x,y,z)
laptop2 = object(x,y,z)
laptop3 = object3(x,y,z)
laptop.setthing(x,y,z)
laptop2.setthing(x,y,z)
laptop3.setthing(x,y,z)

print(laptop)
print(laptop.non_dunder)
print(laptop.dunder)
print(laptop2)
print(laptop2.non_dunder)
print(laptop2.dunder)
print(laptop3)
print(laptop3.non_dunder)
print(laptop3.dunder)
'''
