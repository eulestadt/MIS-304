# Name: Phoenix Wang
# Assignment Number: 7
# Date: 11/16/19
# Section: 9:30-11
# Description: A program to allow the user to select the bread, print it and set the price.
# This is a program made for a bread shop with different options to control for
# inventory, price, and type.

#imports the bread class
import bread

#main program to be executed
def main():
    # initialize variables
    choice = '' # the choice that the user chooses
    breadType = '' # the type of bread that the user chooses
    inventory = 0 # the inventory of the selected bread
    breadPrice = 0 # price of the bread to be set
    breadList = [] # list of all the breads
    priceFlag = 0 # flag for setting the price
    
    #instantiating three bread objects 
    butterBread = bread.Bread("BUTTER", 10, 3.50) #butter bread with an inventory of 10 and price of $3.50
    wheatBread = bread.Bread("WHEAT", 50, 4.00) #wheat bread with an inventory of 50 and price of $4.00
    raisinBread = bread.Bread("RAISIN", 25, 3.50) #raisin bread with an inventory of 25 and a price of $3.50

    #assigning all three objects to a list
    breadList = [butterBread, wheatBread, raisinBread]

    #while loop for decision structure to process the choices
    while choice != 'X':
        #prints header of the program
        print('Welcome to the Blissful Bread Company')
        print('=====================')
        #prints the different menu options
        print('A: Output information for all breads') #option to ouput information on all breads
        print('B: Set a new price for a bread') #option to set a price
        print('C: Output inventory for a specific bread') #option to output inventory
        print('X: Exit the program') #option to exit the program

        #calling a function to prompt the user for the menu choice
        choice = getChoice()
        
        if choice == 'A':
            printAllBreads(breadList)

        #choice for setting the price of the bread
        elif choice == 'B':
            breadType = input('Enter the type of bread you want to set the price of: ').upper()
            breadPrice = float(input('Enter the price you want to set the bread to: '))
            priceFlag = setPrice(breadList, breadType, breadPrice)
            if priceFlag == 0:
                print('The bread type was not found!')


        #choice for if the user chooses C for outputting the inventory of the bread
        elif choice == 'C':
            #prompting the user to input the type of bread they want
            breadType = input('Enter the type of bread you want to check: ').upper()

            #calls the outputBreadInventory function to get the inventory of the bread
            inventory = outputBreadInventory(breadList, breadType)
            
            #checking if the return value is 0 and outputting an error statement if so
            if inventory == 0:
                #tells the user that the bread type is not found
                print('The bread type was not found!')
            #prints the inventory of the bread
            else:
                print('The inventory of', breadType, 'bread is', inventory)

        #choice for if the user exits the program
        elif choice == 'X':
            #thanks the user for using the program
            print('Thank you for breading with Blissful Bread!')

        #checks if the user enters a valid choice
        else:
            #tells the user that they need to enter a valid choice
            print('Please enter a valid choice!')

        #prints a new line at the end of each prompt
        print()

#function to get the choice of the user
def getChoice():
    #prompts the user to enter the choice
    choice = input('Please enter your choice: ').upper()
    #validation loop to check if the user enters a valid choice
    while choice != 'A' and choice != 'B' and choice != 'C' and choice != 'X':
        #notifies the user if they made an invalid choice and prompts to enter again
        choice = input('Invalid input! Please enter your choice: ').upper()
    return choice
        
#sets the price of the bread
def setPrice(breadList, breadType, breadPrice):
    #initialize variables
    breadFound = '' #flag to tell if the bread is found
    breadFound = 'A' #default flag that the bread is not found

    #iterates through list to find correct bread type
    for bread in breadList:
        if breadType == bread.get_breadType():
            #calls set_price to set the bread price
            bread.set_price(breadPrice)
            # set flag to show that the bread is found
            breadFound = 'B'
            break
    # if flag is not set to B, then returns 0
    if breadFound == 'A':
        return 0
    
#outputs the inventory of the bread
def outputBreadInventory(breadList, breadType):
    #initialize variables
    breadFound = '' #flag to tell if the bread is found
    breadFound = 'A' #default flag that the bread is not found

    #iterates through list to find correct bread type
    for bread in breadList:
        if breadType == bread.get_breadType():
            #return the inventory of the bread
            return bread.get_inventory()
            # set flag to show that the bread is found
            breadFound = 'B'
            break
    # if flag is not set to B, then returns 0
    if breadFound == 'A':
        return 0
    
    
#prints all the different types of bread
def printAllBreads(breadList):
    #prints a new line
    print()
    #loops through the breads and prints the attributes of each one
    for bread in breadList:
        print(bread)
        

#calls the main program
main()
