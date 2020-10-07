"""
Tenzin Tsering Shrestha, 27C
reg of a customer with atleast 5 fields,
loop unless user exits,
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
        print("\nEnter new customer details")
        accNum = input('Account number: ')
        firstName = input('First name: ')
        lastName = input('Last name: ')
        age = input('Age: ')
        gender = input('Gender: ')

        # file = open('customerData.txt', 'a')
        data = accNum + ',' + firstName + ',' + lastName + ',' + age + ',' + gender + '\n'
        print(data)
        # file.write(data)
        # file.close()
        if self.fileCommand('sort', data):  # to sort the data in customerData.txt after every new record
            input("Record saved, press Enter to continue.")

    def searchRec(self):
        """ search for records using account number"""
        record = self.fileCommand('search')
        if record != None:
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

    def fileCommand(self, state, newdata=None):
        """ sorts the current data in customerData.txt accordint to ascending order of first names"""
        savedRec = []  # list of current saved data
        nameList = []  # list of all first names in txt file, to be sorted in ascending order
        sortedRec = []  # list for new sorted data
        file = open('customerData.txt', 'r')
        data = file.readlines()
        print(data)
        print(newdata)
        print("")
        file.close()

        for i in data:
            replacedata = i.replace('\n', '')
            medata = replacedata.split(',')
            savedRec.append(medata)
        print("\n", savedRec)
        if newdata != None:
            savedRec.append(newdata)
            print(savedRec, "\n")

        if state == 'sort':
            print("It workes!")
            for i in range(len(savedRec)):  # to sort names in ascending order
                temp = str(savedRec[i][1])
                nameList.append(temp)
            nameList.sort()  # the nameList has been sorted in ascending order
            nameList = list(dict.fromkeys(nameList))  # to remove duplicate values in fnames

            file = open('customerData.txt', 'w')
            for i in range(len(nameList)):  # to sort the current saved records
                print("NEW", i)
                for j in range(len(savedRec)):
                    if nameList[i] == savedRec[j][1]:  # if current name in namelist matches name in savedRec
                        templine = savedRec[j][0] + ',' + savedRec[j][1] + ',' + savedRec[j][2] + ',' + savedRec[j][3] + ',' + savedRec[j][4] + '\n'
                        sortedRec.append(templine)
                        file.write(sortedRec[i])  # write the current line onto txt file
                        print("log:", savedRec[j])
                        print("log:", sortedRec[i],"\n")
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
                searchFactor = input(f"Enter the {searchType} to search for:\n>>")
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
