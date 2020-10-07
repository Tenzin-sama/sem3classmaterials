"""
register a customer with atleast 5 data fields,
loop continuously unless user exits,
user chooses one of the options:
register - data to be saved in file,
search - search using acc number
display - display all records in ascending order of first names
exit - exit the program
"""


class Customer:
    def __init__(self):
        pass

    def main(self):
        """ main method that runs on a continuous loop"""
        print("\nWelcome to the program")
        while True:
            print("\nChoose one of the following options:")
            print("r- register new entry\ns- search saved records\nd- display saved records\ne- exit\n")
            resp = input(">>")
            if resp == 'r':
                self.registerNew()
            elif resp == 's':
                self.searchRec()
            elif resp == 'd':
                self.displayAll()
            elif resp == 'e':
                break
            elif resp == 'q':
                self.fileCommand('sort')  # for testing sort feature
            else:
                print("Incorrect input")

    def registerNew(self):
        """ registration of new customer"""
        print("\nEnter new customer details")
        accNum = input('Account number: ').capitalize()
        firstName = input('First name: ').capitalize()  # to remove problems while sorting
        lastName = input('Last name: ').capitalize()
        age = input('Age: ').capitalize()
        gender = input('Gender: ').capitalize()

        file = open('customerData.txt', 'a')
        data = accNum + ',' + firstName + ',' + lastName + ',' + age + ',' + gender + '\n'
        print("Input:", data)
        file.write(data)
        file.close()
        if self.fileCommand('sort'):  # to sort the data in customerData.txt after every new record
            input("Record saved, press Enter to continue.")

    def searchRec(self):
        """ search for records using first name or accout number"""
        record = self.fileCommand('search')
        if record is not None:
            print(f"\nFound {len(record)} record(s):\nAccNum, Fname, Lname, Age, Gender")
            for i in record:
                print(i)
        else:
            print(f"\nNot Found. Records for searched value does not exist.")

    def displayAll(self):
        """ display all saved records"""
        print("\nAccNum, Fname, Lname, Age, Gender")
        records = self.fileCommand('display')
        for i in range(len(records)):
            print(records[i])  # print all line by line

    def fileCommand(self, state):
        """ sorts the current data in customerData.txt accordint to ascending order of first names"""
        savedRec = []  # list of current saved data in txt file
        nameList = []  # list of all first names in txt file, to be sorted in ascending order
        sortedRec = []  # list for new sorted data
        file = open('customerData.txt', 'r')
        data = file.readlines()
        file.close()

        for i in data:
            replacedata = i.replace('\n', '')
            medata = replacedata.split(',')
            savedRec.append(medata)

        if state == 'sort':
            for i in range(len(savedRec)):  # to sort names in ascending order
                temp = str(savedRec[i][1])
                nameList.append(temp)
            nameList.sort()  # the nameList has been sorted in ascending order
            nameList = list(dict.fromkeys(nameList))  # to remove duplicate values in fnames

            file = open('customerData.txt', 'w')
            n = 0
            fileIndex = 0
            for curName in nameList:
                for i in range(len(savedRec)):
                    if curName == savedRec[i][1]:  # if current name in namelist matches name in savedRec
                        templine = savedRec[i][0] + ',' + savedRec[i][1]
                        templine = templine + ',' + savedRec[i][2] + ',' + savedRec[i][3]
                        templine = templine + ',' + savedRec[i][4] + '\n'
                        sortedRec.append(templine)
                        file.write(sortedRec[fileIndex])  # write the current line onto txt file
                        fileIndex += 1
                n += 1
            file.close()
            return True

        elif state == 'search':
            searchType, pos = "", ""
            foundVal = []
            flow = False
            resp = input("\nSearch using firstname or accnum?:\n1- first name\n2- account number\n>>")
            if resp == '1':
                searchType = 'First Name'
                pos = 1
                flow = True
            elif resp == '2':
                searchType = 'Account Number'
                pos = 0
                flow = True

            if flow:
                searchFactor = input(f"Enter the {searchType} to search for:\n>>").capitalize()
                for j in range(len(savedRec)):
                    if searchFactor == savedRec[j][pos]:  # if current name in namelist matches name in savedRec
                        foundVal.append(savedRec[j])
                return foundVal
            if not flow:
                print("Invalid response.")
                return self.fileCommand('search')

        elif state == 'display':
            return savedRec


a = Customer()
a.main()
