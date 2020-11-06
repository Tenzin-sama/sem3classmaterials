class signup:

    while(True):
        inpt=""
        inpt=input("Enter s for sum number or x to exit \n")
        if inpt=='s':
            a=input("Enter the first number \n")
            b=input("Enter the second number \n")
            sum = int(a)+int(b)
            print("Total=", sum)

        if inpt=='x':
            break

signup()
"""
HW:
reg of a customer with 5 field.
Until customer stop
data to be saved in file
search, display

class customer:
'ask what to do'
register()
    'save data on file'
search()
    'search data with account number'
display()
    'display all data according to ascending order of names'
"""