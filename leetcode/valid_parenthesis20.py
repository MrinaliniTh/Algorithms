def valid_parenthesis(input):
    valid_dict = {"{":"}", "(":")", "[" : "]"}
    stack = []
    for key in input:
        if key in valid_dict:
            stack.append(key)
        elif not stack:
            return False
        else:
            pop_key = stack.pop()
            if key == valid_dict[pop_key]:
                continue
            else:
                return False
    return False if stack else True


print(valid_parenthesis("{{}}"))