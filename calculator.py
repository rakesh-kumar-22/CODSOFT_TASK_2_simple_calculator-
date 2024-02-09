#Task-2 program to create a simple calculator with basic  arithmetic operations

def add(x,y):
    return x+y
def subtract(x,y):
    return x-y
def multiply(x,y):
    return x*y
def divide(x,y):
    if y==0:
        return "Error !while divison by zero."
    else:
        return x/y
    

print("Select Operation")
print("1.Add")
print("2.Subtract")
print("3.Multiplication")
print("4.Division")

ch=int(input("Enter choice(1/2/3/4):"))
num1=float(input("Enter the first number : "))
num2=float(input("Enter the second number : "))
if ch==1:
    print(num1,"+",num2,"=",add(num1,num2))

elif ch==2:
    print(num1,"-",num2,"=",subtract(num1,num2))

elif ch==3:
    print(num1,"*",num2,"=",multiply(num1,num2))

elif ch==4:
    print(num1,"/",num2,"=",divide(num1,num2))

else:
    print("Invalid Input.")