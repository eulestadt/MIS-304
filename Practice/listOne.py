def forLoopExample():
    list = [5, 10, 15, 20, 25]

    writeNumber = open('finalList.txt', 'a')
    for number in list:
        number = number - 4
        print(number)
        textNumber = str(number)
        writeNumber.write(textNumber + '\n')
        
    writeNumber.close()

def whileLoopExample():
    list = [5, 10, 15, 20, 25]
    count = 0
    size = len(list)
    writeNumber = open('finalList.txt', 'a')
    
    while count < size:
        print(list[count])
        list[count] = list[count] - 4
        print(list[count])
        appendElement = str(list[count])
        writeNumber.write(appendElement + '\n')
        count += 1
    writeNumber.close()

def testExample():
    testList = [5, 10, 15, 20, 25]
    testList.append(99)
    print(testList)
    testList.insert(2, 88)
    print(testList)

def listsTwoExample():
    testList = [5, 10, 15, 20, 25]
    testList.append(99)
    print(testList)
    testList.insert(2, 88)
    print(testList)

def copyingLists():
    newList = []
    listToCopy = [1, 2, 3, 4, 5]
    for num in listToCopy:
        newList.append(num)
    print(newList)
    count = 0
    size = len(listToCopy)
    while count < size:
        listToCopy[count] = listToCopy[count] * 10
        count += 1
    print(newList)
    print (listToCopy)


copyingLists()
