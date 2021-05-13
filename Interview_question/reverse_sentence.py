def reverse_sentence(input, res, final_res):
    if not len(input):
        return final_res + res[-1]
    if input[-1] == " ":
        final_res += res[::-1] + " "
        res = ""
    else:
        res += input[-1]
    return reverse_sentence(input[:len(input) - 1], res, final_res)

def count_number_of_words(input):
    count = 0
    i = 0
    while i < len(input):
        if input[i] == ' ':
            if i + 1 <= len(input) - 1 and input[i + 1] != ' ':
                count += 1
        elif i == 0 and input[i] != ' ':
            count += 1
        i += 1
    return count


input = "   I love        my     india    "
# print(reverse_sentence(input, "", "")) #india my love I
print(count_number_of_words(input)) # 4
