fin = open('words.txt', 'r')
for words in fin.readlines():
    length = len(words.strip())
    if length > 20:
        print (words)


fin.close()