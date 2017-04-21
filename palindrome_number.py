num = raw_input("Enter any number: ") 
rev_num = reversed(num) 
# check if the string is equal to its reverse 
if list(num) == list(rev_num): 
             print("Palindrome number") 
else: 
             print("Not Palindrome number")
