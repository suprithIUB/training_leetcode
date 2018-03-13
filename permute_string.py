def permute(string):
    if not string:
        return
    counter = 0
    for i in range(0, len(string)):
        word = ""
        permute_helper(string[:i] + string[i+1:], word + string[i], counter)
        print()

def permute_helper(string, word, counter):
    if not string:
        print(counter, word)
        return

    for i in range(0, len(string)):
        permute_helper(string[:i] + string[i+1:], word + string[i], counter)

permute("abcdef")
