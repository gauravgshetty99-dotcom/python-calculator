n=10
m=5
operation=input("enter operation(+,-,*,/):")
if operation=="+":
    print(n+m)
elif operation=="-":
    print(n-m)
elif operation=="*":
    print(n*m)
elif operation=="/":
    print(n/m)
else:
    print("invalid operation:")
#KEEPS THE TERMINAL OPEN UNTIL YOU PRESS ENTER AGAIN
input("\nPress enter to exit...")
