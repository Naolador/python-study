from random import randrange


def dcompare(t):
    length = len(t)-1
    count = 0
    for i in range(length):
        if t[i] == t[i+1]:
            count += 1
            i += 2
        else:
            i += 1
        if count == 2:
            return True


def birth_days():
    bday_list = []
    for i in range(23):
        bday = randrange(1,365)
        bday_list += [bday]
    compare(bday_list)

print(birth_days())