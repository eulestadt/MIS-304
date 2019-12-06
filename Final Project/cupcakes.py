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
        #checks if price is positive
        if price < 0:
            print('Invalid price! Price must be positive!')
        else:
            self.__price = price

    #set_flavor method receives the cupcake object and flavor
    #sets the flavor attribute of the cupcake
    def set_flavor(self, flavor):
        self.__flavor = flavor

    #set_inventory method 
    def set_inventory(self, inventory):
        # check if inventory is <= 0 or > 100
        if inventory <= 0 or inventory > 100:
            print('Invalid inventory quantity! Please enter a value between 0 and 100')
        #sets the inventory of the bread
        else:
            self.__inventory = inventory
            
    #__str__ method returns a string with all the attributes of the cupcake
    def __str__(self):
        #creates a string with the value of all the attributes
        selfString = 'The cupcake price is $' + str(format(self.__price, '.2f')) + '\n' + 'The cupcake flavor is ' + self.__flavor + '\n' + 'The cupcake inventory is ' + str(self.__inventory) + '\n'

        #returns the value of all outputs
        return selfString

#class for the cupcake with topping
class CupcakeWithTopping(Cupcake):
    #inherits all attributes from cupcake with the additional topping attribute
    def __init__(self, price, flavor, inventory, topping):
        Cupcake.__init__(self, price, flavor, inventory)
        self.__topping = topping

    #gets the topping of the cupcake
    def get_topping(self):
        return self.__topping

    #set the topping of the cupcake
    def set_topping(self, topping):
        self.__topping = topping

    def __str__(self):
        return Cupcake.__str__(self) + 'The cupcake topping is ' + self.__topping + '\n'
    
                 
