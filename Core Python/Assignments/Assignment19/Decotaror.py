# Q.1. Develop a memoization decorator that caches the results of function
# calls and returns the cached result when the same inputs occur again.
# This can greatly improve the performance of recursive or
# computationally intensive functions.


def memoize(func):
    cache = {}
    
    def wrapper(*args):
        if args in cache:
            return cache[args]
        
        result = func(*args)
        cache[args] = result
        return result
    return wrapper
@memoize
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

print("Fibonacci of 35: ",fibonacci(35))  # Computes and caches quickly
