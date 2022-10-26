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
from Laptops import *

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

