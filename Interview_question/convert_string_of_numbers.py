# i/p :: "10345"
# o/p :: "10000+300+40+5"

def convert_into_string_of_digits(input):
    res = ""
    total = len(input) - 1
    for i in range(len(input)):
        if input[i] != '0':
            res += input[i]
            temp_no = total - i
            while temp_no > 0:
                res += '0'
                temp_no -= 1
            if i != total:
                res += '+'
    return res

print(convert_into_string_of_digits("10345"))