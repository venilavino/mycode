arrnumbers = []
n = 0
a = 0
sum = 0
 
print "Total Numbers:", 
n = input()
 
for i in range (0, n):
   print "Enter", i + 1, "Number: ", 
   a = input()
   arrnumbers.append(a)
   sum += a
 
print "The sum of numbers: [", 
for i in range (0, n):
   print arrnumbers[i],  
 
print " ] is: ", sum
