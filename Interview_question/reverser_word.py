# approach 1
def reverse_word(s1):
    final_string = ""
    res = ""
    for i in range(len(s1)):
        if s1[i] == ' ':
            final_string = final_string[::-1]
            res += final_string + " "
            final_string = ''
            continue
        final_string += s1[i]
    return res + final_string
# approach 2
def reverse_word2(sentence):
    stack = []
    res = ''
    for i in range(len(sentence)):
        stack.append(sentence[i])
        if sentence[i] == ' ':
            while stack:
                res += stack.pop()
    return res + " " + "".join(stack)[::-1]

sentence = "He is a nice guy"
print(reverse_word2(sentence))
ans = "eH si a ecin yug"