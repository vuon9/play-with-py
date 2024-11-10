def factorial(n):
    result = 1
    while n > 1:
        result *= n
        n -= 1
    return result

def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

# print(factorial(5))
print(fibonacci(6))