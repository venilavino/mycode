def is_prime(x):
    if x > 1:
        n = x // 2
        for i in range(2, n + 1):
            if x % i == 0:
                return False
        return True
    else:
        return False

num = input("Enter any number: ")
if is_prime(num):
    print str(num) + " is a prime number"
else:
    print str(num) + " is not a prime number"
