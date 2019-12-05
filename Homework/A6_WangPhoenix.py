# Name: Phoenix Wang
# Assignment Number: 6
# Date: 10/31/19
# Section: 9:30 - 11
# Description: The program reads a file that contains information about cakes
# for multiple names, prices, profit margins, and quantity. The program calculates
# the profit and revenue and then utilizes a two dimensional list to store the values
# that is also outputted to the user.

# global constants
NUMROW = 5 # number of rows per record

# main function of the program
def main():
    # initialize variables
    twoDim = [] # two dimensional list 

    #handling exceptions and errors
    try:
        # open the cake file
        cakesFile = open('HW6_FILE.txt', 'r')

        #read the first line of the cakes file and assigns it to cakeName
        cakeId = cakesFile.readline().rstrip('\n')

        #executes the following while there is still data to be read
        while cakeId != '':
            #initialize variables
            prodList = [] #list to store the product information
            maxRow = 0 #storing the count of the number of rows
            cakeName = '' #variable to store the name of the cake
            cakePrice = 0 #variable to store the price of the cake
            cakeMargin = 0 #variable to store the profit margin of the cake
            cakeQuantity = 0 #varible to store the quantity of cake

            #reading the cake file into variables
            cakeName = cakesFile.readline().rstrip('\n') #reads the cake name and assigns it to a variable
            cakePrice = float(cakesFile.readline()) #reads the cake price and assigns it to a variable
            cakeMargin = float(cakesFile.readline()) #reads the cake profit margin and assigns it to a variable
            cakeQuantity = int(cakesFile.readline()) #reads the cake quantity and assigns it to a variable

            #appending the items from the cake file into the cake list
            prodList.append(cakeId) #appends the cake ID onto the cake list
            prodList.append(cakeName) #appends the cake name onto the cake list
            prodList.append(cakePrice) #appends the cake price onto the cake list
            prodList.append(cakeMargin) #appends the cake profit margin onto the cake list
            prodList.append(cakeQuantity) #appends the cake quantity onto the 

            #appending the cake list to a two dimensional list
            twoDim.append(prodList)

            #keeping a count of how many rows have been appended
            maxRow += 1

            #calling the product report
            prodReport(prodList)
            
            #read the cake file into the cakeId
            cakeId = cakesFile.readline().rstrip('\n')

        # closes the data file
        cakesFile.close()    
    #handling the IOError and outputting a message
    except  IOError:
        print('There was an error in reading the file! Please make sure the file is EmployeeRecords.txt')

    #handling all other errors, outputting the system message
    except  Exception as err:
        print("There was an error! The system message is: ", err)

    # calls the printTwoDim function to print the two dimensional array 
    printTwoDim(twoDim)

# function that takes an argument of a list of all the products and prints each individual one
def prodReport(productList):
    # initialize variables
    itemIndex = 0 #index of the item
    revenue = 0 #index of the item
    profit = 0 #profit of the item
    
    # while loop to iterate through and print the product list
    while itemIndex < NUMROW:
        #prints the item in the product list at the index value
        print(productList[itemIndex])
        itemIndex += 1

    # calculate the revenue by multiplying the cake quantity and price
    revenue = productList[2] * productList[4]

    # calculate the profit by multiplying the revenue and profit margin
    profit = revenue * productList[3]

    #prints the revenue and cake profit
    print ('The Revenue is $', format(revenue, '.2f'), sep='')
    print ('The Cake Profit is $', format(profit, '.2f'), '\n', sep='')
    
# function that takes an argument of a two dimensional list and outputs the list
def printTwoDim(twoDimensionList):
    
    #initialize variables
    r = 0 # the count for iterating the rows of the list
    c = 0 # the count for iterating the columns of the list
    numRows = 0 # the number of rows of the list
    numCols = 0 # the number of columns of the list

    #calculate the number of rows and number of columns
    numRows = len(twoDimensionList) # finds the number of rows in the list
    numCols = len(twoDimensionList[0]) # finds the number of columns in the list

    #prints the section header 
    print('The content of the two dimensional list :')

    # loop to iterate through all the rows
    while r < numRows:
        
        # loop to iterate through all the columns
        while c < numCols:
            
            #prints the value of the item in the list at the index position
            print(twoDimensionList[r][c])

            #adds 1 to the column count
            c += 1
        #adds 1 to the row count
        r += 1
        # resets the count to 0
        c = 0

        #prints a new line
        print()

# executes the main program
main()
