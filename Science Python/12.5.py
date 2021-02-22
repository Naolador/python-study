def has_match(t1, t2):
    for x, y in zip(t1, t2):
        if x == y:
            print(f"Found match: {x}")
    return False

t1=[1, 2, 5, 7, 3]
t2=[3, 5, 9, 8, 3]

print(has_match(t1,t2))