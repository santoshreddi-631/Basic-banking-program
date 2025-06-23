#Banking
def check_balance(balance):                                         #Fetching bank balance
    print("*****************************************")
    print(f"Your available balance is ${balance:.2f}")
    print("*****************************************")


def deposit():                                                       #Adding money to your account
    amount = float(input("Enter an amount to be deposit: "))
    if amount <0:
        print("***********************")
        print("That not a valid amount")
        print("***********************")
        return 0
    else:
        print("***************")
        print("Deposit Success")
        print("***************")
        return amount



def withdraw(balance):                                               #Withdrawn money from your account
    amount = float(input("Enter the amount to be withdrawn: "))
    if amount > balance:
        print("*******************")
        print("Insufficient funds!")
        print("*******************")
        return 0
    elif amount<0:
        print("***************************")
        print("Amount mus be grater than 0")
        print("***************************")
        return 0
    else:
        print("*****************")
        print("Withdraw Success!")
        print("*****************")
        return amount



def main():                                                          #Main function
    balance = 0
    is_running = True

    while is_running:
        print("***************************")
        print("Welcome to our Bank")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")
        print("***************************")

        choice = input("Enter the service as you want (1-4): ")
        if choice == '1':
            check_balance(balance)
        elif choice == '2':
            balance +=deposit()
        elif choice == '3':
           balance -= withdraw(balance)
        elif choice == '4':
            is_running = False
            print("**********************")
            print("Thank You! Visit Again")
            print("**********************")
        else:
            print("********************")
            print("Enter a valid choice")
            print("********************")

if __name__ == '__main__':
    main()