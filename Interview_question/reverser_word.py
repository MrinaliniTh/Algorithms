# approach 1
def reverse_word(str1):
    final_string = ""
    res = ""
    i = 0
    s1 = len(str1)
    while i < s1:
        if str1[i] == ' ':
            if i + 1 < s1 and str1[i+1] == ' ':
                i += 1
            else:
                if final_string:
                    final_string = final_string[::-1]
                    res += final_string + " "
                    final_string = ''
                    i += 1
                else:
                    i += 1
        else:
            final_string += str1[i]
            i += 1
    return res + final_string[::-1] if final_string else res[0:len(res)-1]


# approach 2, using stack
def reverse_word2(sentence):
    stack = []
    res = ''
    for i in range(len(sentence)):
        stack.append(sentence[i])
        if sentence[i] == ' ':
            while stack:
                res += stack.pop()
    return res + " " + "".join(stack)[::-1]

sentence = "      He   is   a          nice   guy "
print(reverse_word(sentence))
ans = "eH si a ecin yug"