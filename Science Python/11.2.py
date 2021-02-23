def histogram(s):
    d = dict()
    for c in s:
#        print(c)
        d[c] = d.get(c, 0) + 1
#        print(d[c])
    return print_hist(d)

def print_hist(d):
    print(d)
    for c in sorted(d):
#        print(c.strip())
        print(c, d[c])
    exit(0)

h = histogram('aloha')

print(h)

#https://realpython.com/python-histograms/