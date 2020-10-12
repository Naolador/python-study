e_count = 0
no_e_count = 0


def has_no_e(word):
    global e_count
    global no_e_count
    if 'e' in word:
        print(f"find 'e' in {word}")
        e_count += 1
    else:
        print(f"{word} does not have 'e'")
        no_e_count += 1
    print(f"e_count:{e_count}\nno_e_count:{no_e_count}")


fin = open('words.txt')

for words in fin.readlines():
    has_no_e(words.strip())

total = e_count + no_e_count
pct = round((no_e_count / total) * 100, 2)
print(f"The percentage of no e is {pct}%")
fin.close()
