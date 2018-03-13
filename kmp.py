def prefix_array(pattern):
    if not pattern:
        return
    prefix_array = [0] * len(pattern)

    i = 1
    j = 0
    while i < len(pattern):
        print(prefix_array)
        if pattern[i] == pattern[j]:
            prefix_array[i] = j+1
            i += 1
            j += 1
        else:
            if j != 0:
                j = prefix_array[j-1]
            else:
                i += 1

    print prefix_array
    return prefix_array

def kmp():
    s = "abcxabcdabcdabcy"
    pattern = "abcdabcy"
    lps = prefix_array(pattern)
    i = 0
    j = 0
    while j < len(lps) and i < len(s):
        if pattern[j] == s[i]:
            i += 1
            j += 1
        elif j >= 1:
            j = lps[j-1]
        elif j >= 0:
            i += 1
    return j == len(pattern)

prefix_array("abaab")
print(kmp())
