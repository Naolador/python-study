def reverse_lookup(k,v):
    for c in k:
        if k[c] == v:
            print(f"{v} in English is {c}")
            exit(0)
    raise LookupError()

def dict(v):
    eng2sp={'one':'uno','two':'dos','three':'tres'}
    return reverse_lookup(eng2sp,v)


print(dict('uno'))