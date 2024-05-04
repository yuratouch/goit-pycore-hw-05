from collections import defaultdict

def caching_fibonacci(n) -> int:
    cache = defaultdict(int)

    def fibonacci(n) -> int:
        if n <= 0:
            return 0
        elif n == 1: 
            return 1
        elif n in cache:
            return cache[n]
        else:
            cache[n] = fibonacci(n - 1) + fibonacci(n - 2)

        return cache[n]

    return fibonacci(n)

print(caching_fibonacci(10))  # Виведе 55
print(caching_fibonacci(15))  # Виведе 610
