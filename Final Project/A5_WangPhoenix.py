# Name: Phoenix Wang
# Assignment Number: 5
# Date: 10/25/19
# Section: 9:30 - 11
# Description: The program reads a file that contains employee files for multiple
# employees and their salaries for January through March. The program parses the file
# and prints the employee's salary for each of the months and prints the calculated
# lowest monthly salary and average monthly salary for each employee.

def main():
    # initialize variables
    employeeName = '' # employee name
    employeeSalaryJan = 0 # employee salary for the month of January
    employeeSalaryFeb = 0 # employee salary for the month of February
    employeeSalaryMar = 0 # employee salary for the month of March

    #handling exceptions and errors
    try:
        # open the employee records file
        employeeData = open('EmployeeRecords.txt', 'r')

        # read the first line of the employee records and assign to employee name
        employeeName = employeeData.readline().rstrip('\n')

        # executes the following while there is still data to be read
        while employeeName != '':
            # declaring an empty list to store salary information
            salaryList = [] # list of the employee name and salaries 
            salaryOnlyList = [] # list of only the employee salaries
            minimumSalary = 0 # minimum monthly salary for the employee
            averageSalary = 0 # average monthly salary for the employee

            # initialize constants
            MONTHS_NUMBER = 3 # three months of salaries per employee
            
            # converts the next line to a float and stores the value in employeeSalaryJan
            employeeSalaryJan = float(employeeData.readline())
            # converts the next line to a float and stores the value in employeeSalaryFeb
            employeeSalaryFeb = float(employeeData.readline())
            # converts the next line to a float and stores the value in emploeeSalaryMar
            employeeSalaryMar = float(employeeData.readline())

            # appending the employee name to the list
            salaryList.append(employeeName)
            # appending the employee salaries to the list
            salaryList.append(employeeSalaryJan)
            salaryList.append(employeeSalaryFeb)
            salaryList.append(employeeSalaryMar)


            # prints the name of the employee
            print ('Employee: ', employeeName, sep='')

            # prints the employee salary for January
            print('January: $', format(employeeSalaryJan, '.2f'), sep='')

            # prints the employee salary for February
            print('February: $', format(employeeSalaryFeb, '.2f'), sep='')

            # prints the employee salary for March
            print('March: $', format(employeeSalaryMar, '.2f'), sep='')

            # new list with only salary values
            salaryOnlyList = salaryList[1:3]
            # finding the minimum salary
            minimumSalary = min(salaryOnlyList)

            # prints the lowest monthly salary 
            print('The lowest monthly salary is: $', format(minimumSalary, '.2f'), sep = '')

            # calling the average salary function to find the average employee salary
            averageSalary = calculateAverageSalary(salaryList, MONTHS_NUMBER)
            
            # prints the average monthly salary
            print('The average monthly salary for ', employeeName, ' is: $', format(averageSalary, '.2f'), '\n', sep='')
                        
            # reads the next line for the employee name 
            employeeName = employeeData.readline().rstrip('\n')

        # closes the data file
        employeeData.close()

    #handling the IOError and outputting a message
    except  IOError:
        print('There was an error in reading the file! Please make sure the file is EmployeeRecords.txt')

    #handling all other errors, outputting the system message
    except  Exception as err:
        print("There was an error! The system message is: ", err)    

# function to calculate the average salary of the employee
# receives the arguments of a list of salaries and a value for the number of months
# returns the average salary of the employee
def calculateAverageSalary(salaries, numberOfMonths):
    #initialize variables
    countSalary = 1 # the index for the salary in the list. starting count at 1 since the first item is the name of the employee
    listSize = 0 # the size of the list
    totalSalaries = 0 # the total of all the salaries
    averageSalary = 0 # the calculated average salary

    # finding the size of the list and assigning the size to a variable
    listSize = len(salaries) 

    # while loop to itereate through the salaries
    while countSalary < listSize:
        # adds the value in the list to the total salaries
        totalSalaries += salaries[countSalary]
        # add to the count of the salary
        countSalary += 1

    # calculates the average salary
    averageSalary = totalSalaries / numberOfMonths

    #returns the average salary for the employee
    return averageSalary

# executes the main function
main()
