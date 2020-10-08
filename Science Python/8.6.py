def find(word,letter,pos=0):
    index = pos
    while index < len(word):
        if letter == word[index]:
            print(f"found {letter}")
            return
        index+=1
    return -1

print(find('apple','a',1))