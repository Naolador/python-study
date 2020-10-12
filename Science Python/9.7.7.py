def is_repeat(word):
    count = 0
    i = 0
    j = i + 1
    k = len(word) - 1
    if k >= 6:
        while j <= k:
            if word[i] == word[j]:
#                print(f"Hit: {word[i]} in {word}")
                count += 1
            i += 1
            j += 1

    if count == 3:
        return True


file = open('words.txt', 'r')
for word in file.readlines():
    if is_repeat(word.strip()):
        print (f"Horray! I found it:{word}")
