savedRec = []  # list of current saved data
nameList = []  # list of all first names in txt file, to be sorted in ascending order
sortedRec = []  # list for new sorted data
file = open('0testfile.txt', 'r')
data = file.readlines()
file.close()

for i in data:
    replacedata = i.replace('\n', '')
    medata = replacedata.split(',')
    savedRec.append(medata)

for i in range(len(savedRec)):  # to sort names in ascending order
    temp = str(savedRec[i][1])
    nameList.append(temp)
nameList.sort()  # the nameList has been sorted in ascending order
nameList = list(dict.fromkeys(nameList))  # to remove duplicate values in fnames
print(nameList)
print(len(savedRec))
for i in range(len(savedRec)):
    print(i)
file = open('0testfile.txt', 'w')

n = 0
fileIndex = 0
for curName in nameList:
    for i in range(len(savedRec)):
        if curName == savedRec[i][1]:  # if current name in namelist matches name in savedRec
            templine = savedRec[i][0] + ',' + savedRec[i][1] + ',' + savedRec[i][2] + ',' + savedRec[i][3] + ',' + savedRec[i][4] + '\n'
            sortedRec.append(templine)
            file.write(sortedRec[fileIndex])  # write the current line onto txt file
            fileIndex += 1
    n += 1
file.close()
