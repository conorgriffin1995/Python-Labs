# remove duplicates from a list
def unique_list(l):  
  x = []  
  for a in l:  
    if a not in x:  
      x.append(a)  
  return x  
  
print(unique_list([1,2,3,3,3,3,4,5]))

# split a string into words, sort, and join back with
def sort(string):
    string.split()   # into a list
    return '-'.join(sorted(string))

print(sort('hfr pon cb'))

# perfect number
def perfect_number(n):  
    sum = 0  
    for x in range(1, n):               # to n - 1
        if n % x == 0:                  # proper divisor
            sum += x  
    return sum == n 
print(perfect_number(6))

# a function that determines if a number is a perfect number
n = int(input("Enter any number: "))
def isPerfect(n):
    sum1 = 0
    for i in range(1, n):
        if(n % i == 0):
            sum1 = sum1 + i
    if(sum1 == n):
        print("The number is a perfect number!")
    else:
        print("The number is not a Perfect number!")

print(isPerfect(n))

# a function which determines if a number is a prime number
num = int(input("Enter any number: "))
def test_prime(num):
    if(num==1):
        return False
    elif (num==2):
        return True
    else:
        for x in range(2,num):
            if(num % x==0):
                return False
            return True
print(test_prime(num))

# function which returns the reverse of a string
def reverse(string):
    return string[::-1]

# a function that determines if a string is a palindrome
def test_palindrome(string):
    # call reverse function
    rev = reverse(string)
    if (string == rev):
        return True
    else:
        return False

print(test_palindrome('malayalam'))

# iterative
# function to check string is 
# palindrome or not 
def isPalindrome(str):
 
    # Run loop from 0 to len/2 
    for i in xrange(0, len(str)/2): 
        if str[i] != str[len(str)-i-1]:
            return False
    return True

print(isPalindrome('malayalam'))

# a function to claculate the nth fibonacci number recursively
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

print(fib(10))

# write a function which multiplies the numbers in list by each other
from functools import reduce
def sum(data):
    s = 0
    for i in data:
        s = s * i
    return s

print(sum([1, 2, 3]))







































