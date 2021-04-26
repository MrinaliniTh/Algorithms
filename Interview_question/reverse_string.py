def reverse_string(word, res):
    if not word:
        return res
    res += word[-1]
    return reverse_string(word[:len(word)-1], res)
print(reverse_string("Mrinalini", ""))