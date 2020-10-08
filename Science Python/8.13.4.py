def rotate_word(string, shift):
    new_string=[]
    for char in string:
        tonum=ord(char)
        newnum=tonum+shift
        tochar=chr(newnum)
        new_string.append(tochar)
    return new_string


print(rotate_word("IBM", -1))