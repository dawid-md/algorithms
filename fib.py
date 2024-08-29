def getnFib(n):    
    a = 0
    b = 1

    for j in range(n):
        z = a
        a = b
        b = a + z

    return z

print(getnFib(10))