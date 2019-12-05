# Name: Phoenix Wang
# Assignment Number: 7
# Date: 11/16/19
# Section: 9:30-11
# Description: Implementing a Bread class that is defined with
# the attributes of bread type, inventory of bread, and
# the price of bread and allows for the set and get of each attribute.

class Bread:
    #__init__ method accepts an argument for the bread type, inventory, and price
    def __init__(self, breadType, breadInventory, breadPrice):
        #asssigns the bread type to the breadType attribute
        self.__breadType = breadType
        #asssigns the bread inventory to the breadInventory attribute
        self.__breadInventory = breadInventory
        #asssigns the bread price to the breadPrice attribute
        self.__breadPrice = breadPrice

    #set_breadType method allows the user to set the bread type
    def set_breadType(self, breadType):
        self.__breadType = breadType
        
    #set_inventory method allows the user to set the inventory
    def set_inventory(self, inventory): 
        # check if the inventory is negative or zero and prints an error message if so
        if inventory <= 0:
            print('Invalid inventory quantity! Please enter a value greater than 0')
        #sets the inventory of the bread
        else:
            self.__breadInventory = inventory
            
    #set_price method allows the user to set the price
    def set_price (self, price):
        # check if the price is negative or zero and prints an error message if so 
        if price <= 0:
            print('Invalid price. Please enter a positive price!')

        # check if price is above $5.50 and returns an error message if so
        elif price > 5.50:
            print('Invalid price. Please enter a price less than $5.50!')

        # sets the price of the bread
        else:
            self.__breadPrice = price

    #get_breadType method returns the bread type
    def get_breadType(self):
        return self.__breadType
    
    #get_invetory method returns the bread inventory
    def get_inventory(self):
        return self.__breadInventory

    #get_price method returns the bread price
    def get_price(self):
        return self.__breadPrice

    #the __str__ method returns a string indicating all the attributes of the bread
    def __str__(self):
        #creates a string with the value of all the attributes 
        selfString = 'The bread type is ' + self.__breadType + '\n' + 'The inventory of bread is ' + str(self.__breadInventory) + '\n' + 'The price of bread is $' + format(self.__breadPrice,'.2f') + '\n'

        #returns the value of all outputs
        return selfString

    
