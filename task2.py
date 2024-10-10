def calculate(number1,number2,operation):
    if operation == "+":
        return number1+number2
    elif operation=="-":
        return number1-number2
    elif operation=="*":
        return number1*number2
    elif operation=="/":
        if number2!=0:
            return number1/number2
        else:
            return "Error"
    elif operation=="%":
        if number2!=0:
            return number1%number2
        else:
            return "Error"    
    else:
        return "Enter the correct Operation"
def cal():
    print("Calculator")
    try:
        number1=float(input("Enter First Number: "))
        number2=float(input("Enter Second Number: "))
    except ValueError:
        print("Invalid Input")
        return
    operation=input("\nEnter the Operation Symbol (+,-,*,/,%):")
    result=calculate(number1,number2,operation)
    print(f"The result of {number1} {operation} {number2} is: {result}")
if __name__=="__main__":
    cal()