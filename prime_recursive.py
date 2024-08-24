def primeNumber(n):
    if n < 2:
        return n
    return primeNumber(n-1) + primeNumber(n-2)

print(primeNumber(3))