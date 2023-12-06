# 1st Pyhton Project
# A Basic Banking System
# OKANE BANK
import fontstyle  # used for to access different font styles(to modify the text)

# early mistake solved
# def accountin():  # function to input account no.
#     accnum = input("Enter your account no.: ")
#     return accnum
bank_info = {}
""" Creating dictionary to store bank_info
    Reason dictionary is used over lists:
                    1.It allows us to give a unique id to a value
                    2.It is easier to associate certain values to main(key) value
                    3.Lists are unable to maintain or have any relationship among the values present"""

while True:
    print(' ' * 50, fontstyle.apply("WELCOME TO OKANE BANK!!!", "BOLD/YELLOW"))


    def accountcheck():  # function to check if account no is correct
        accnum = input("Enter your account no.: ")  # we'll try to hide user input(status:Not working right now
        if len(accnum) == 14:  # check length
            if accnum.isdigit():  # check if its only digits
                print("Account no. is correct.")
            else:
                print("Account no. should only contain digits!")  # if anything other than digits are entered
                # To read input again and re-check account no.
                print("Please re-enter the account no. ")
                accountcheck()
        else:
            print("Account no. should have only 14 digits!")  # if length of account no. exceeds 14
            # To read input again and re-check account no.
            print("Please re-enter your account no. ")
            accountcheck()
        return accnum


    rightaccnum = accountcheck()


    # working with the given account no.
    def account_details():
        # displaying account details
        print(fontstyle.apply("Account Details:", "BOLD/UNDERLINE"))
        print("Name:", bank_info[rightaccnum]['name'])
        print("Account number:", bank_info[rightaccnum]['accountno'])
        print("Branch:", bank_info[rightaccnum]['branch'])
        print("Balance:", bank_info[rightaccnum]['balance'])


    if rightaccnum not in dict.keys(bank_info):
        bank_info[rightaccnum] = {}  # using nested dictionary
        # this dictionary should possess:1.Name 2.account number 3.branch 4.balance in the account
        print(fontstyle.apply("Enter your account details:", "BOLD/UNDERLINE"))
        bank_info[rightaccnum]['name'] = input("Enter account holder's name: ")
        bank_info[rightaccnum]['accountno'] = rightaccnum
        bank_info[rightaccnum]['branch'] = input("Enter the branch: ")
        bank_info[rightaccnum]['balance'] = 0
        account_details()
    else:
        print(' ' * 50, fontstyle.apply("WELCOME BACK", "BOLD/YELLOW"))
        account_details()
    print(fontstyle.apply("What service do you require:", "BOLD/UNDERLINE"))
    print("Enter 1 for Withdrawal")
    print("Enter 2 for Deposit")


    def withdraw():#for withdrawing required amount
        if bank_info[rightaccnum]['balance'] == 0:
            print(fontstyle.apply("Insufficient balance!!", "RED"))
            acc_opt()
        else:
            amt = int(input("Enter amount to be withdrawn:"))
            if amt > bank_info[rightaccnum]['balance']:
                print(fontstyle.apply("Insufficient funds!!\n Re enter amount", "RED"))
                withdraw()
            else:
                bank_info[rightaccnum]['balance'] -= amt


    def deposit():#for depositing mentioned
        amt = int(input("Enter amount to be deposited:"))
        if amt > 5000000:
            print(fontstyle.apply("Exceeds the limit\nRe enter amount", "RED"))
            deposit()
        else:
            bank_info[rightaccnum]['balance'] += amt


    def acc_opt():#to accept choice between withdrawal or deposit
        accopt = int(input("Enter your choice:"))
        if accopt == 1:
            withdraw()
        elif accopt == 2:
            deposit()
        else:
            print(fontstyle.apply("Incorrect choice\nRe enter choice", "RED"))
            acc_opt()


    acc_opt()
    account_details()
    #asks user if they want to exit
    choice = input("Do you wish to exit?: ")
    choice.lower()
    if choice == "yes":
        print(' ' * 50, fontstyle.apply("Thank you for your time!!!!", "YELLOW"))
        exit()
