def cumsum(t):
    total = sum(t)
    t.append(total)
    return t

t = [1, 2, 3]

print(cumsum(t))