import string

def is_palindrome(number):
    
    if len(number) == 1 or len(number) == 0:
        return True
    elif(number[0] == number[-1]):
        return is_palindrome(number[1:-1])
    
    return False


def sequential_decrementing(number):
    
    for x in range(len(number) - 1):
        if int(number[x]) - 1 != int(number[x + 1]):
            return False 
    return True

def sequential_increasing(number):
    
    for x in range(len(number) - 1):
        if int(number[x]) + 1 != int(number[x + 1]):
            if x == len(number) - 2:
                if number[x] == '9' and number[x + 1] == '0':
                    return True
            return False
    return True

def same(number):
    for x in range(len(number) - 1):
        if number[x] != number[x+1]:
            return False
    return True

def same_after_first(number):
    for x in range(1, len(number)):
        if number[x] != '0':
            return False
    return True

def in_list(number, number_list):
    for x in number_list:
        if int(number) == x:
            return True
    return False

print(is_palindrome('1590'))
print(sequential_decrementing('1590'))
print(sequential_increasing('67890'))
print(same('1590'))
print(same_after_first('1590'))
print(sequential_decrementing('1590'))
