def fibonacci():
    first, second = 1, 1
    yield first
    yield second
    
    while True:
        third = first + second
        yield third

        first, second = second, third

for n in fibonacci():
    print(n)
