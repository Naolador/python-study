def error_msg():
    print("ERROR: You must enter a valid letter!")
    exit(-1)


def rotate_letter(letter, n):
    if letter.isupper():
        start = ord('A')
    elif letter.islower():
        start = ord('a')
    else:
        error_msg()
    n_letter = ord(letter)
    shift = ((n_letter - start) + n) % 26
    new_n = start + shift
    new_letter = chr(new_n)
    return new_letter


def rotate_word(word, n):
    str = ''
    for letter in word:
        str += rotate_letter(letter, n)
    return str


print(rotate_word('IBM', -1))
