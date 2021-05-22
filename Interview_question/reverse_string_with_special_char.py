special_characters = "!@#$%^&*()-+?_=,<>/"
def reverse_string_with_special_char(input):
    temp = [0] * len(input)
    num = len(input) - 1
    for i in reversed(range(len(input))):
        print(i, num-i, len(temp))
        if input[num-i] in special_characters:
            print(input[num-i])
            temp[i + num -i]= input[num-i]
            # temp[i]= input[i]
        else:
            temp[num-i]= input[i]
    return temp

input = "Bubli#and&Saumya@"
print(reverse_string_with_special_char(input)) #"aymua#Sdn&ailbuB@"