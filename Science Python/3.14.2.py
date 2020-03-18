def print_spam(arg):
    print(arg)


def do_twice(prt,arg):
    prt(arg)
    prt(arg)

def do_forth(prt,arg):
    do_twice(prt,arg)
    do_twice(prt,arg)

do_forth(print_spam, 'spam2')

