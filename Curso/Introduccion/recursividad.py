# 5! = 5 * 4! = 120
# 4! = 4 * 3 * 2 * 1 = 24
# N! = N * (N-1)!

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

def run():
    n = 5
    print(f'Factorial de {n} es {factorial(n)}')
    
run()    

# Fibonacci 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55
# F(n) = F(n-1) + F(n-2)

def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

def runFibo():
    n = 8
    print(f'Fibonacci de {n} es {fibonacci(n)}')
    
runFibo()


def addNumberSequence(n):
    if n == 0:
        return 0
    return n + addNumberSequence(n - 1)

def runAddNumberSequence():
    n = 100
    print(f'Suma de los primeros {n} números es {addNumberSequence(n)}')
    
runAddNumberSequence()