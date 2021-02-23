from random import randrange


def is_duplicate(t):
    s = t
    s.sort()
#    print(s)
    for i in range(len(s)-1):
        if s[i] == s[i+1]:
            return True
    return False

def ran_bdays(n):
    t = []
    for i in range(n):
        bday = randrange(1, 365)
        t += [bday]
    return t

def count_matches(num_students, num_simulations):
    count = 0
    for i in range(num_simulations):
        t = ran_bdays(num_students)
        if is_duplicate(t):
            count += 1
    return count


def main():
    num_students = 23
    num_simulations = 1000
    count = count_matches(num_students,num_simulations)

    print(f"After {num_simulations} of simulations with {num_students} students, we found {count} simulations with at least one match!")

main()