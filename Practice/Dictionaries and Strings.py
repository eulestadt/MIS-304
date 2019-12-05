def dictionaries():
    #initialize variables
    phonebook_dict = {'Jenny':'501-2619','John':'506-4521'}
    for key in phonebook_dict:
        print(key)
        print(phonebook_dict[key])
    del phonebook_dict['Jenny']
    for key in phonebook_dict:
        print(key)
        print (phonebook_dict[key])

def Strings():
    stringVar = "Long long ago"
    for ch in stringVar:
        print(ch)
        ch = 'A'
        print(ch)
    print(stringVar)

def stringIndex():
    stringVar = "Long long time ago"
    index = 0
    while index < len(stringVar):
        print(stringVar[index])
        print(stringVar[index])
        index += 1
    print(stringVar)

def inClass():
    stringVar = input('Enter integer number')
    if stringVar.isdigit():
        stringVar = int(stringVar)
        stringVar += 3
        print(stringVar)
    else:
        print('Not a string!')

def slice():
    stringVar = 'John Jacob Twice'
    firstName = stringVar[0:4]
    lastName = stringVar[-5:]
    print(firstName, ' ', lastName)

def search():
    rhyme = 'Mary had a little lamb'
    if 'has' in rhyme:
        print("Has is in rhyme")
    else:
        print("has is not in rhyme")

def split():
    rhyme = "Mary had a little lamb"
    rhymeList = rhyme.split()
    for word in rhymeList:
        print(word)

def countLambs():
    count = 0 
    lambs = 'Mary had a little lamb little lamb little lamb'
    lambList = lambs.split()
    for word in lambList:
        if word == "lamb":
            count += 1
        print (word)
        print (count)

def countLambWhile():
    count = 0
    listIndex = 0
    listLength = 0
    lambs = 'Mary had a little lamb little lamb little lamb'
    lambList = lambs.split()
    listLength = len(lambList)
    while listIndex < listLength:
        if lambList[listIndex] == "lamb":
            print(lambList[listIndex])
            count += 1
        else:
            print('not a lamb')
        listIndex += 1
    print (count)
    
def listPractice():
    listValues = [1, 2, 3, 4, 5]
    newList = []
    for num in listValues:
        newList.append(num)
    index = 0
    while index < len(newList):
        newList[index] = newList[index] + 1
        index += 1
    print (newList)

