def has_duplicates(t):
    length=len(t)
    t.sort()
    i=0
    while i < length-1:
        print(i)
        if t[i] == t[i+1]:
            return True
        i += 1
    return False

t=[1, 2, 3, 4, 5, 6, 1]

print(has_duplicates(t))