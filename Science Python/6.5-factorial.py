def factorial(n):
    if not isinstance(n, int):
        print("Factorial is only defined for integers!")
        exit(1)
    elif n < 0:
        print("Factorial is not defined for negative integers!")
        return None
    elif n == 0 or n == 1:
        return 1
    else:
        recurse = factorial(n - 1)
        result = recurse * n
        print(result)
        return result


print(f"result is {factorial(5)}")
