def factorial(n):
    if n == 0:
        return 1
    else:
        recurse = factorial(n-1)
        result = recurse * n
        return result

n=factorial(4)
print (n)