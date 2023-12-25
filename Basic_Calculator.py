while True:
    num1=int(input("Enter 1st Number: "))
    num2=int(input("Enter 2nd Number: "))
    Operator=(input("Enter The Operator(+,-,*,/): "))
    if Operator=="*":
        print(num1*num2)
    elif Operator=="/":
        print(num1/num2)
    elif Operator=="-":
        print(num1-num2)
    elif Operator=="+":
        print(num1+num2)
    else:
        print("Invalid Operation")
