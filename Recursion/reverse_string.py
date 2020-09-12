def reverse_string(string:str)-> str:
    size = len(string)
    if size == 0:
        return 
    last_char = string[size - 1]
    print(last_char, end = "")
    reverse_string(string[0:size - 1])

reverse_string('GOOGLE')