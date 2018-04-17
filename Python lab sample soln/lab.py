# perfect number
def perfect_number(n):  
    sum = 0  
    for x in range(1, n):               # to n - 1
        if n % x == 0:                  # proper divisor
            sum += x  
    return sum == n  
print(perfect_number(6))

# remove duplicates from a list
def unique_list(l):  
  x = []  
  for a in l:  
    if a not in x:  
      x.append(a)  
  return x  
  
print(unique_list([1,2,3,3,3,3,4,5]))


# split a string into words, sort, and join back with -
def sort(string):
	words = string.split(' ')       # into a list
	words.sort()  
	return '-'.join(words)
	
print(sort('hello there world'))

# prime number test by trial division
def test_prime(n):  
    if (n==1):  
        return False  
    elif (n==2):  
        return True  
    else:  
        for x in range(2,n):  
            if(n % x==0):  
                return False  
        return True               
print(test_prime(5))  

# sum up the numbers in a list - iterative

from functools import reduce
def sum(data):
    sum = 0
    for i in data:
        sum += i
    return sum

print(sum([1, 2, 3]))


# implement a function which multiplies the numbers in list by each other, ignoring items in the
# list which are zero
# e.g. [3, 0, 5] gives 15
# [2, 4, 5] gives 40
# use reduce

def product(a, b):
    if (a == 0) and (b == 0):
        return 0
    elif (a == 0) and (b != 0):
        return b
    elif (a != 0) and (b == 0):
        return a
    else:
        return a * b

ans = reduce(product, [3, 0, 5] )
print (ans)

# or use filter to filter out 0s
ans = reduce(product, filter(lambda i: i != 0, [3, 5, 0]))
print (ans)

# define a function which calculates n factorial
# factorial - recursive
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(10))

# initialise a list of digits and map factorial to the list
digits = list(range(1, 10))
factorial_digits = map(factorial, digits)
print (list(factorial_digits))

# implement a function which counts the number of words in a list
# of words excluding the words 'the', 'is', and 'and'
stopwords = ['the', 'is', 'and']

def count(a, b):
    if (b not in stopwords):
        return a + 1
    else:
        return a

text = ['hello', 'there', 'world', 'python', 'and', 'functional']
wordcount = reduce(count, text, 0)
print (wordcount)

# or
print(len([word for word in text if word not in stopwords]))

# implement a function using a closure which allows the day of week in english or irish to be
# determined for a specified day number (1 .. 7)
# the function take the language as an input and returns a function
# which takes the day number as input

def day_of_week(language):
    if language == "english":
        days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    else:
        days = ['Luain', 'Mhairt', 'Cheadaoin', 'Deardoin', 'Aoine', 'Satharn', 'Domhnach']
    def day(n):
        if n >=1 and n <= len(days):
            return days[n-1]
        else:
            raise Exception
    return day

day = day_of_week("english")
print(day(2))
day = day_of_week("irish")
print(day(2))


