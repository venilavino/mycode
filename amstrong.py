print("Enter the number")
number = int(input())
temp = int(number)
Sum = 0

while(temp != 0):
    rem  = temp % 10 
    Sum  = Sum + (rem * rem * rem) 
    temp = temp / 10 

if(number == Sum):
    print ("Armstrong Number")
else:
    print ("Not an Armstrong Number")
