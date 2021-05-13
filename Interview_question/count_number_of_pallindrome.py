def count_number_of_pallindrome(sentence):
    count = 0
    res = ""
    i = 0
    while i < len(sentence):
        while i < len(sentence) - 1 and sentence[i + 1] != " ":
            res += sentence[i]
            i += 1
        res += sentence[i]
        if res == res[::-1]:
            count += 1
            i += 1
        i += 1
        res = ""
    return count

print(count_number_of_pallindrome("wow beb bn great"))