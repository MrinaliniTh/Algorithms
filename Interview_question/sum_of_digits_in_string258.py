# input: "abc345gh8mm3"
# output: 3+4+5+8+3 = 23 => 2 + 3 = 5

def add_digits(words):
    num = ""
    for s in words:
        try:
            if int(s):
                num += s
        except Exception:
            continue
    num = int(num)
    while num >= 10:
        question = num // 10
        remainder = num % 10
        num  = question + remainder
    return num


print(add_digits("abc345gh8mm3"))