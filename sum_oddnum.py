start = 0
end = 0
sum = 0
n = 0
 
print "Enter Starting Number:", 
start = input()
print "Enter Ending Number:", 
end = input()
 
n = start
if ( (n  % 2) == 0):
   n += 1
 
print "Adding Numbers : ", 
while(n <= end):
   print n, 
   sum += n
   n += 2
 
print "\nThe result is: ", sum


