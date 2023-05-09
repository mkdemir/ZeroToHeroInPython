def user__login():

    print("""
    ************************
    User Login Programing
    ************************
          """)
    
    sys_username = "mkdemir"
    sys_password = "12345"

    login_fail_count = 3

    while True:
        username = input("Username: ")
        password = input("Password:  ")

        if(username != sys_username and password == sys_password):
            print("Username is wrong...")
            login_fail_count -= 1
        elif(username == sys_username and password != sys_password):
            print("Password is wrong...")
            login_fail_count -= 1
        elif(username != sys_username and password != sys_password):
            print("Username and Password are wrong...")
            login_fail_count -= 1
        else:
            print("Successful Login")
            break
        if (login_fail_count == 0):
            print("You've run out of entry rights...")
            break

def atm_machine():

    print("""
    **************************
    Welcome to the ATM Machine

    Operations:

    1. Balance Inquiry
    2. Deposit Money
    3. Withdrawal of Money

    Press "q" to exit the program
    **************************
    """)


    balance = 1000

    while True:
        operation = input("Select the process: ")
        if (operation == 'q'):
            print("We are waiting again")

            break
        elif (operation == '1'):
            print(f'Balance is ${balance}')

        elif (operation == '2'):
            amount = int(input('Enter Amount'))
            balance += amount
            print(f'Balance is ${balance}')

        elif (operation == '3'):
            print(f'Balance is ${balance}')
            amount = int(input('Enter Amount: '))

            if (balance - amount < 0):
                print("Cannot withdraw such an amount")
                continue
            balance -= amount
            print(f"Balance is ${balance}")

        else:
            print("Invalid Operation")
            pass

            
if __name__  == "__main__":
    # user__login()
    atm_machine()
