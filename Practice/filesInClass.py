def main():
    totalGrade = 0 # total grade of all the students
    average = 0 # average grade of all the students
    count = 0 # count of all the grades
    studentInformation = open('studentNamesAndGrades.txt', 'r')
    studentName = studentInformation.readline().rstrip('\n')
    while studentName != '':
        grade = studentInformation.readline()
        print(studentName, ' has an average grade of ', grade, sep='')
        grade = float(grade)
        totalGrade += grade
        count += 1
        studentName = studentInformation.readline().rstrip('\n')
    average = totalGrade/count
    studentInformation.close()

    print('The average grade is', average)


# the while loop moves forward because of 

def mainSure():
    totalGrades = 0
    count = 0
    averageGrade = 0
    studentNamesAndGrades = open('studentNamesAndGrades.txt', 'r')
    studentName = studentNamesAndGrades.readline().rstrip('\n')
    while studentName != '':
        grade = float(studentNamesAndGrades.readline())
        print(studentName, 'has an average grade of', grade)
        totalGrades += grade
        count += 1
        studentName = studentNamesAndGrades.readline().rstrip('\n')
    averageGrade = totalGrades / count
    print('the average grade is', averageGrade)

mainSure()
