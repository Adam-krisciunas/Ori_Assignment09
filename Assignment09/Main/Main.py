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

from LaptopsPackage import *

laptop = Laptops('Silver', 825) #i don't know why it doesn't like this!!!

laptop.setPrice(-1000)
laptop.setPrice(800) #non-dunder example
laptop.setprice(950)
laptop.setPrice(1200)

laptop.setPrice(975) #non-dunder example
print(laptop.__str__()) #dunder example
laptop.checkcolor("White")
print(laptop.__str__()) #dunder example

myLaptops = [laptop('Black', 875), # these are the actual peak heights of these mountains
              laptop('Pink', 1050),
              laptop('Blue', 1500)]

# traverse the list and print the data
for laptop in myLaptops:
    print(laptop.__repr__())
