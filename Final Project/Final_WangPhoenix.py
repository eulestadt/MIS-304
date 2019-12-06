# Name: Phoenix Wang
# Assignment Number: 7
# Date: 11/16/19
# Section: 9:30-11
# Description: A program that allows the user to to adjust the amount of cupcakes 

#imports the cupcakes class
import cupcakes

#main program to be executed
def main():
    #initialize variables
    continueChoice = '' #user choice for continuing
    choice = '' #choice of menu option
    cupcakeList = [] #list of all the cupcakes
    price = 0 #price of the cupcake
    inventory = 0 #inventory of the cupcake
    topping = '' #topping of the cupcake
    
    continueChoice = 'yes' #set loop to continue

    #instantiating five cupcake objects
    #instantiating the blueberry cupcake
    blueberryCupcake = cupcakes.Cupcake(7.50, 'blueberry', 22)
    #instantiating the strawberry cupcake
    strawberryCupcake = cupcakes.Cupcake(3.50, 'strawberry', 15)
    #instantiating the blackberry cupcake
    blackberryCupcake = cupcakes.Cupcake(7.00, 'blackberry', 10)

    #instantiating the chocolate cupcake
    chocolateCupcake = cupcakes.CupcakeWithTopping(5.5, 'chocolate', 30, 'chocolate chips')
    #instantiating the vanilla cupcake
    vanillaCupcake = cupcakes.CupcakeWithTopping(4.5, 'vanilla', 40, 'crushed peanuts')

    #adding the cupcakes into a list
    cupcakeList = [blueberryCupcake, strawberryCupcake, blackberryCupcake, chocolateCupcake, vanillaCupcake]

    #while loop for decision structure to process the choices
    while continueChoice == 'yes':
        #call function to display the menu
        choice = displayMenu()

        
        #if the user chooses choice A
        if choice == 'A':
            #calls the retrieveCupcake function
            cupcake = retrieveCupcake(cupcakeList)

            #checks if the cupcake was found
            if cupcake == 0:
                print('The cupcake has not been found!')
            #if cupcake is found
            else:
                #asks the user to enter a price for the cupcake
                price = float(input('Enter the price for the cupcake: '))

                #sets the price of the cupcake
                cupcake.set_price(price)

        #if the user chooses choice B
        elif choice == 'B':
            #calls the retrieveCupcake function
            cupcake = retrieveCupcake(cupcakeList)
            #checks if the cupcake has been found
            #if cupcake isn't found, tells the user
            if cupcake == 0:
                print('The cupcake has not been found!')
            else:
                #checks if the cupcake is a CupcakeWithTopping
                if isinstance(cupcake, cupcakes.CupcakeWithTopping):
                    #asks the user to enter a topping for the cupcake
                    topping = input('Enter the new cupcake topping: ')

                    #sets the topping of the cupcake
                    cupcake.set_topping(topping)
                    
                #if no topping, tells the user that there is a 
                else:
                    print('This type of cupcake does not have a topping!')

        #if the user chooses C
        elif choice == 'C':
            #calls the retrieveCupcake function
            cupcake = retrieveCupcake(cupcakeList)

            #checks if the cupcake has been found
            #if cupcake isn't found, tells the user
            if cupcake == 0:
                print('The cupcake has not been found!')
            #if cupcake is found
            else: 
                #asks the user to enter the inventory of the cupcake
                inventory = int(input('Enter the new inventory for the cupcake: '))

                #sets the inventory of the cupcake
                cupcake.set_inventory(inventory)
            
        #if the user chooses D
        elif choice == 'D':
            print('Cupcake Report')
            print('==============')
            #loops throuh the cupcakes and prints the attributes of each one
            for cupcake in cupcakeList:
                print(cupcake)

        #asks if the user would like to continue the program
        continueChoice = input('Would you like to continue (yes or no)? ').lower()


#displays the menu and returns the valid result
def displayMenu():
    choice = '' #initialize variables
    #prints header of the cupcake menu
    print('Welcome to the Cupcake Menu')
    print('=======================')
    #prints the different options
    print('A-Change price') #change price option
    print('B-Update Topping') #update topping option
    print('C-Update Inventory') #update inventory option
    print('D-Print All cupcakes') #print all option

    #asks the user to input their choice
    choice = input('Please enter your choice: ').upper()

    #validation loop to check if user enters valid choice
    while choice != 'A' and choice != 'B' and choice != 'C' and choice != 'D':
        #notifies the user if they made an invalid choice and prompts to enter again
        choice = input('Invalid input! Please enter your choice: ').upper()

    #returns the choice
    return choice

def retrieveCupcake(cupcakeList):
    #initialize variables
    flavor = ''
    cupcakeFound = 'A' #default cupcake is not found

    #prompts user to input the flavor
    flavor = input('Enter the flavor that you would like: ').lower()

    
    #iterates through list to find correct cupcake type
    for cupcake in cupcakeList:
        
        #checks if the flavor match
        if flavor == cupcake.get_flavor():
            
            #notifies the user that the cupcake is found
            print('The Cupcakes has been found!')
            
            #prints the cupcake information
            print(cupcake)

            #returns the cupcake object
            return cupcake
        
            # set flag to show that the cupcake is found
            cupcakeFound = 'B'

            #break out of the loop
            break
        
    # if cupcake is not set to B, then returns 0
    if cupcakeFound == 'A':
        return 0
    
main()
    
