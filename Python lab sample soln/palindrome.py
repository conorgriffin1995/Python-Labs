# write a python function which determines whether a string is
# a palindrome
# both iteratively and recursively

# palindrome

def isPalindrome1(string):  
    left_pos = 0  
    right_pos = len(string) - 1  
    while right_pos >= left_pos:  
        if not string[left_pos] == string[right_pos]:  
            return False  
        left_pos += 1  
        right_pos -= 1  
    return True  

print(isPalindrome1('navan'))

# recursive version
def isPalindrome2(string):  
    if len(string) <= 1:
        return True
    else: 
        if string[0] == string[-1]:
            return isPalindrome2(string[1:-1])
        else:
            return False                                   

print(isPalindrome2('navan'))


       
