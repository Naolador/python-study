def uses_only(word):
    string = 'acefhlo'
    word=word.replace(" ","")
    for letter in word:
        if letter in string:
            continue
        else:
            print (f"Error: {letter} is not allowed in the list!")
            exit(-1)
    return True

value = input("Please enter a string: ")
uses_only(value)