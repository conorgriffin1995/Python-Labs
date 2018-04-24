# 1) function that sums up the numbers in a list using an iterative approach
def sum_list(l):
	sum = 0
	for element in l:
		sum+=element
	return sum
print("Question 1: sums up numbers in a list")
print(sum_list([3,5,6,2]))


# 2) remove duplicates from a list
def unique_list(l):  
  x = []  
  for a in l:  
    if a not in x:  
      x.append(a)  
  return x  
print("Question 2: remove duplicates from list")
print(unique_list([1,4,8,1,8,2,3,3,3,3,4,5]))

# 3) split a string into words, sort, and join back with -
print("Question 3: split a string into words, sort and join back")
def sort(string):
    string.split()   # into a list
    return '-'.join(sorted(string))

print(sort('hfr pon cb'))

# split a string into words, sort, and join back with -
def sort(string):
	words = string.split(' ')       # into a list
	words.sort()  
	return '-'.join(words)
	
print(sort('hello there world'))

# 4) perfect number
def perfect_number(n):  
    sum = 0  
    for x in range(1, n):               # to n - 1
        if n % x == 0:                  # proper divisor
            sum += x  
    return sum == n 
print("Question 4: Perfect number")
print(perfect_number(6))

# a function that determines if a number is a perfect number
print("Question 4: function that determines if a number is a perfect number")
#n = int(input("Enter any number: "))
def isPerfect(n):
    sum1 = 0
    for i in range(1, n):
        if(n % i == 0):
            sum1 = sum1 + i
    if(sum1 == n):
        print("The number is a perfect number!")
    else:
        print("The number is not a Perfect number!")
print(isPerfect(28))

# a function which determines if a number is a prime number
print("Question 5: function that determines whether a number is a prime number")
#num = int(input("Enter any number: "))
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
print(test_prime(21))

# function which returns the reverse of a string
def reverse(string):
    return string[::-1]

# a function that determines if a string is a palindrome
print("Question 6: Function to determine if a string is a palindrome")
def test_palindrome(string):
	print("Testing string: " + string)
	# call reverse string
	rev = reverse(string)
	if(string == rev):
		return True
	else:
		return False
print(test_palindrome('lool'))

# recursive version
print("Question 6: RECURSIVE VERSION")
def isPalindrome2(string):  
    if len(string) <= 1:
        return True
    else: 
        if string[0] == string[-1]:
            return isPalindrome2(string[1:-1])
        else:
            return False                                   

print(isPalindrome2('navan'))

# a function to calculate the nth fibonacci number recursively
print("Question 7: Function to calculate the nth fibonacci number recursively")
def fib(n):
	if n == 0:
		return 0
	elif n == 1:
		return 1
	else:
		return fib(n-1) + fib(n-2)
print(fib(10))

# write a function which multiplies the numbers in list by each other,
# ignoring items in the list which are zero
# use reduce() and supply function you have written.
# then implement an alternative solution using filter()
# importing functools for reduce()
from functools import reduce
print("Question 8: a function which multiplies the numbers in list by each other," +
	 " ignoring items in the list which are zerouse reduce()"
	 + " and supply function you have written.")
def product(a, b):
	if(a == 0) and (b == 0):
		return 0
	elif (a == 0) and (b != 0):
		return b
	elif (a != 0) and (b == 0):
		return a
	else:
		return a * b

ans = reduce(product, [3, 0, 5])
print(ans)

# or use filter to filter out 0s
ans = reduce(product, filter(lambda i: i != 0, [3, 5, 0]))
print("Using filter")
print(ans)

# a function which calculates n! (factorial) using recursion.
print("Question 9: a function which calculates n! (factorial) using recursion.")
def factorial(n):
	if n == 0:
		return 1
	else:
		return n * factorial(n-1)
print(factorial(4))

# initialise a list of digits and map factorial to the list
digits = list(range(1,10))
factorial_digits = map(factorial, digits)
print(list(factorial_digits))

print("Question 10: a function which counts the number of words in a list of words," 
	  + " excluding the words 'the', 'is' and 'and'")
import re
stopwords = ["the", "is", "and"]
value = ["hello", "is", "the"]
def count_words(l, m):
	if(m not in stopwords):
		return l + 1
	else:
		return l
wordcount = reduce(count_words, value, 0)
print(wordcount)	

language = input("Enter language: ")
n = int(input("Enter number of day of week: "))
def day_of_week(language):
	if language == "english" or language == "English" or language == "ENGLISH":
		days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
	else:
		days = ['Luain', 'Mhairt', 'Cheadaoin', 'Deardoin', 'Aoine', 'Satharn', 'Domhnach']
	def day(n):
		if n >= 1 and n <= len(days):
			return days[n-1]
		else:
			raise Exception
	return day
day = day_of_week(language)
print(day(n))