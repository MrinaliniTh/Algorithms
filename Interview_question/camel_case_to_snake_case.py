def camel_case_to_snake_case(word):
    temp = word[0].lower()
    for i in range(1, len(word)):
        if word[i].isupper():
            temp += "_" + word[i].lower()
        else:
            temp += word[i]
    return temp

print(camel_case_to_snake_case("MacOS"))

