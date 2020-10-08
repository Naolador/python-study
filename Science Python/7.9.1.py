def get_squrt(a, x):
    epsilon = 0.0000001
    while True:
        y = (x + a / x) / 2
        if abs(x - y) < epsilon:
            break
        else:
            x = y
    return y


print(get_squrt(6, 7))
