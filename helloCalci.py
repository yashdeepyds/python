print("Calculator")

choice='y'
while(choice=='y' or choice=='Y'):
    print("Enter the first number")
    x=int(input())
    print("Enter the second number ")
    y=int(input())
    print("Press 1-Addition \t 2-Subtraction \t 3-Multiplication \t 4-Division ")
    print("select the operation")
    ch=int((input()))
    if ch==1:
        print(x+y)
    elif ch==2:
        print(x-y)
    elif ch==3:
        print(x*y)
    elif ch==4:
        print(x/y)
    else:
        print("Invalid choice")
    print("press y to continue or n to terminate")
    choice= input()
print("Come again")

