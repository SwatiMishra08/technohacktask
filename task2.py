#basic calculator
#addition
def add(n1,n2):
    return n1+n2
#subtraction
def sub(n1,n2):
    return n1-n2
#multiplication
def mul(n1,n2):
    return n1*n2
def div(n1,n2):
    return n1/n2
print("Select operation")
print("1.+\n"
      "2.- \n"
      "3.* \n"
      "4./ \n" )
#option for user to select operation
operation=int(input("Enter you choice of operation 1/2/3/2: "))
#taking input from user
n1=float (input("Enter the first number: "))
n2=float(input("Enter the second number: "))
#conditional statement to make operation as per user
if operation==1:
    print(n1,"+", n2, "=" ,add(n1,n2))
elif operation==2:
    print(n1,"-", n2, "=" ,sub(n1,n2))
elif operation==3:
    print(n1,"*", n2, "=" ,mul(n1,n2))
elif operation==4:
    print(n1,"/", n2, "=" ,div(n1,n2))
else:
    print("Invalid input")
