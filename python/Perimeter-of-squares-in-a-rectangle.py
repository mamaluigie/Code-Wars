def fib(n): 
    key = [1,1]
    temp = 0
    if n > 2:
        for x in range(n):
            temp = key[0] + key[1]
            key[0] = key[1]
            key[1] = temp
            
        return key[1] - 1
    else:
        return 1
def perimeter(n):   
    # your code
    return 4 * fib(n + 1)
