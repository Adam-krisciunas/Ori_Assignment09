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
from LaptopsPackage.DellClass import *
from LaptopsPackage.MacBookClass import *

lenovoLaptop = Lenovo('Silver', 825) #this wont work needs fixed

lenovoLaptop.setPrice(-1000)
lenovoLaptop.setPrice(800) #non-dunder example
lenovoLaptop.setPrice(950)
lenovoLaptop.setPrice(1200)

lenovoLaptop.setPrice(975) #non-dunder example
print(lenovoLaptop.__str__()) #dunder example
lenovoLaptop.setcolor("White")
print(lenovoLaptop.__str__()) #dunder example

myLaptops = [Lenovo('Black', 875),
             Lenovo('Pink', 1050),
              Lenovo('Blue', 1500)]

for laptop in myLaptops:
    print(laptop.__repr__())
    
from LaptopsPackage.MacBookClass import *

laptop2 = MacBook('Black', 1000)

print(laptop2.__str__())
print(laptop2.__repr__())
print(laptop2.availability(3))
print(laptop2.availability(0))
print(laptop2.checkcolor())
laptop2.setPrice(1200)
print(laptop2.getPrice())


DellLaptop = Dell('Silver', 825) #this wont work needs fixed

DellLaptop.setPrice(-1)
DellLaptop.setPrice(999)
print(DellLaptop.getPrice())
DellLaptop.setPrice(750)
print(DellLaptop.Dell_sell())
DellLaptop.setPrice(1000)
print(DellLaptop.Dell_sell())
DellLaptop.setPrice(1050)

DellLaptop.setPrice(900) 
print(DellLaptop.__str__()) 

#More lists
myLaptops = [Dell('Black', 999),
             Dell('Pink', 10),
             Dell('Blue', 2)]


for DellLaptop in myLaptops:
    print(DellLaptop.__repr__())
    
    