def calculate_factorial(n):
    #for 0 and 1 return 1
    if n == 0 or n == 1:
        return 1
    
    #initial factorial
    factorial = 1
    
    #calculte factorial
    for i in range(2, n + 1):
        factorial *= i

    return factorial

print(calculate_factorial(8))