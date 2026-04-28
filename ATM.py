balance=0
def deposit():

    global balance
    try:
        amount=float(input("enter the amount :"))
        if amount>0:
            balance+=amount
            print(f"Successfully deposited {amount}.")
        else:
            print("Invalid amount")
    except ValueError:
        print("invalid input, please enter a number")
def withdrawal():
    global balance
    try:
        amount=int(input("enter withdraw amount:"))
        if amount > balance():
            print("Insufficient Balance!!")
        else:
            balance-=amount
            print(f"Successfully withdrew {amount}.")
    except ValueError:
        print("Invalid input,please enter a number.")
def check_balanace():
    print(f"Balance amount:{balance}")
def main():
    
    while True:
        print("---ATM---")
        print("1.DEPOSIT")
        print("2.WITHDRAW")
        print("3.BALANCE EQUIRY")
        print("4.EXIT")
        choice=int(input("Enter the choice(1-4):"))

        if choice==1:
            deposit()
        elif choice==2:
            withdrawal()
        elif choice==3:
            check_balanace()
        elif choice==4:
            print("Thankyou for using ATM Service!!!")
            break
        else:
            print("Invalid choice!!")
main()