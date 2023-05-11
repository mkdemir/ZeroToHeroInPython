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

def factorial():

    print("""
    Factorial Bulma
    
    Çıkmak için q'ya basınız
    """)
    
    # print(*range(2,6))

    while True:
        number = input("Number: ")
        if (number == "q"):
            print("Program Terminated")
            break
        else:
            number = int(number)

            factorial_temp = 1

            for i in range(2, number+1):
                print(f"Faktöriyel: {factorial_temp}; i: {i}")
                factorial_temp *= i
            print("**************************")
            print("Faktöriyel: ", factorial_temp)

def fibonacci():
    """
    # For Döngüsü ile Fibonacci Serisi

    Fibonacci Seri yeni bir sayıyı önceki iki sayının toplamı şeklinde oluşturur.
    1,1,2,3,5,8,13.....
    """
    temp_a = 1
    temp_b = 1

    fibonacci_list = [temp_a,temp_b]

    for i in range(10):
        print(f"i: {i}. a: {temp_a}; b: {temp_b}")
        temp_a, temp_b = temp_b, temp_a + temp_b
        fibonacci_list.append(temp_b)
    print(fibonacci_list,)

if __name__  == "__main__":
    # user__login()
    # atm_machine()
    # factorial()
    fibonacci()
