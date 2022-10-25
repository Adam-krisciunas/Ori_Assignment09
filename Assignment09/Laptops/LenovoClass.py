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

class Lenovo():
    def setPrice(self, price):
        if price < 0:
            print("The price of a Lenovo Laptop cannot be negative")
        else:
            self.price = price;
   
    def checkcolor(self, color):
        self.color = color
        
    def Lenovo_sell(self, sell):
        self.sell = sell
       
    def  __init__ (self, color, price ): # self means current object
        self.color = color;
        self.price = price;
       
    def __str__ (self):
        return "The Lenovo color is  " + self.color + ", the price is "  + str(self.price) + 'dollars'
   
    def __repr__ (self):
        return "color = " + self.color + ",  price = " + str(self.price) + 'dollars'