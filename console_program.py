class ConsoleProgram:
    def __init__(self):
        self.acc_number = ""
        self.first_name = ""
        self.last_name = ""
        self.address = ""
        self.phone_number = ""


    def create_account(self):
        with open('accounts.txt', 'a+') as f:
            f.write("Account Number: "+self.acc_number+"\n")
            f.write("First Name: "+self.first_name+"\n")
            f.write("Last Name: "+self.last_name+"\n")
            f.write("Address: "+self.address+"\n")
            f.write("Phone Number: "+self.phone_number+"\n")
            f.write(" \n")

    def search_profile(self, acc_no):
        with open('accounts.txt', 'r') as f:
            # print(f.readlines()[2])s
            for line_no, line in enumerate(f.readlines()):
                f.seek(0)
                if line[0:15] == "Account Number:":
                    if line[16:-1] == acc_no:
                        for i in range(0,5):
                            f.seek(0)
                            print(f.readlines()[line_no+i])
                else:
                    continue

    def run(self):
        print('Welcome to National Bank!')

        while True:
            option = int(input('What would you like to do: \n1.Create Account \n2.Search for your profile \n3.Quit \nPress 1, 2 or 3.\n'))
            
            if option == 1:
                self.acc_number = input('Please enter your new account number\n')
                self.first_name = input('Please enter your first name\n')
                self.last_name = input('Please enter your last name\n')
                self.address = input('Please enter your address\n')
                self.phone_number = input('Please enter your phone_number\n')
                self.create_account()
                print('Your new account number is '+self.acc_number)

            elif option == 2:
                self.confirm_acc_no = input('Please enter your account number to see profile\n')
                self.search_profile(self.confirm_acc_no)

            elif option == 3:
                print('Program Ended. Thank You!\n')
                break
            
            else:
                print('Invalid choice. Please press 1, 2 or 3.\n')


program = ConsoleProgram()
program.run()
