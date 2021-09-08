def LongestWord(sen):
    i = sen.split()
    longest_word = max(i, key=len)
    sen = longest_word
    return sen


# keep this function call here
print(LongestWord(input()))
