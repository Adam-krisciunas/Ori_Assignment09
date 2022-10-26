'''
Name: Ori Group
email: brattomn@mail.uc.edu, mainalda@mail.uc.edu, krisciag@mail.uc.edu, laupi@mail.uc.edu
Assignment: Assignment 09
Course: IS 4010
Semester/Year: Fall 2022
Brief Description: This project demonstrates that I can use Eclipse to create a PyDev project
Citations:
Anything else that's relevant:
'''

from LaptopsPackage.LenovoClass import *

laptop = Lenovo('Silver', 825) #this wont work needs fixed

laptop.setPrice(-1000)
laptop.setPrice(800) #non-dunder example
laptop.setPrice(950)
laptop.setPrice(1200)

laptop.setPrice(975) #non-dunder example
print(laptop.__str__()) #dunder example
laptop.setcolor("White")
print(laptop.__str__()) #dunder example

myLaptops = [Lenovo('Black', 875),
             Lenovo('Pink', 1050),
              Lenovo('Blue', 1500)]

# traverse the list and print the data
for laptop in myLaptops:
    print(laptop.__repr__())
    
from LaptopsPackage.MacBookClass import *

laptop2 = MacBook('Black', 1000)

print(laptop2.__str__())
print(laptop2.__repr__())
print(laptop2.availability(3))
print(laptop2.availability(0))
