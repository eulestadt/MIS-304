#cupcake class for cupcakes that are sold at the cupcake shop
class Cupcake:

    #receives the arguments of price, flavor, and inventory
    #assigns to the price, flavor, and inventory attributes
    def __init__(self, price, flavor, inventory):
        #assigns the price argument to the price attribute
        self.__price = price
        #assigns the flavor argument to the flavor attribute
        self.__flavor = flavor
        #assigns the inventory argument to the inventory attribute
        self.__inventory = inventory

    #methods to "get" each of the attributes
        
    #gets the price for the cupcake
    #get_price method receives the cupcake object and returns the price
    def get_price(self):
        return self.__price

    #gets the flavor for the cupcake
    #get_flavor method receives the cupcake object and returns the flavor
    def get_flavor(self):
        return self.__flavor

    #gets the inventory for the cupcake
    #get_inventory method receives the cupcake object and returns the inventory
    def get_inventory(self):
        return self.__inventory
    
    #methods to set each of the attributes
    #set_price method receives the cupcake object and price 
    #sets the price attribute of the cupcake
    def set_price(self, price):
        self.__price = price

    #set_flavor method receives the cupcake object and flavor
    #sets the flavor attribute of the cupcake
    def set_flavor(self, flavor):
        self.__flavor = flavor

    #set_inventory method 
    def set_inventory(self, inventory):
        
        self.__inventory = inventory
    #
    def __str__():
        #
        
