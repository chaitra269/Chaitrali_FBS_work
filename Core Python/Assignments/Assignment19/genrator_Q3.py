# Q.3. Write a generator function that mimics the behavior of the built-in
# range() function. The generator should take start, stop, and step
# arguments and yield numbers within the specified range.


def custom_range(start, stop=None, step=1):
    if stop is None:
        stop = start
        start = 0
        
    if step == 0:
        raise ValueError("custom_range() arg 3 must not be zero")
    current = start
    
    if step > 0:
        while current < stop:
            yield current
            current += step
    else:
        while current > stop:
            yield current
            current += step

print("Custom range (1, 10, 2):")
print(list(custom_range(1, 10, 2)))

print("Custom range countdown (5, 0, -1):")
print(list(custom_range(5, 0, -1)))

