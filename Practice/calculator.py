def add():
    print("---ADDITION---")
    num1=float(input("enter the first number:"))
    num2=float(input("enter the second number:"))
    sum=num1+num2
    print("the sum of",num1,"and",num2,"is:",sum)

def subtract():
    print("---SUBTRACTION---")
    num1=float(input("enter the first number:"))
    num2=float(input("enter the second number:"))
    diff=num1-num2
    print("the difference of",num1,"and",num2,"is:",diff)

def multiply():
    print("---MULTIPLICATION---")
    num1=float(input("enter the first number:"))
    num2=float(input("enter the second number:"))
    product=num1*num2
    print("the product of",num1,"and",num2,"is:",product)

def divide():
    print("---DIVISION---")
    num1=float(input("enter the first number:"))
    num2=float(input("enter the second number:"))
    quotient=num1/num2
    print("the quotient of",num1,"and",num2,"is:",quotient)

def main():
    print("***CALCULATOR***")
    while True:
        print("\n 1.ADDITION"
              "\n 2.SUBTRACTION"
              "\n 3.MULTIPLICATION"
              "\n 4.DIVISION" 
              "\n 5.EXIT")
        choice=int(input("Enter The Choice (1-5)"))
        if choice==1:
            add()
        elif choice==2:
            subtract()
        elif choice==3:
            multiply()
        elif choice==4:
            divide()
        elif choice==5:
            print("goodbye!!!")
            break
        
        else:
            print("Invalid choice!!")
def login():
    print("Login_Phase")
    usern=input("USERNAME:")
    passw=input("PASSWORD:")
    if usern=="ilovnigga" and passw=="67":
        main()
    else:
        print("Wrong!!!,Go away ..." )

login()
