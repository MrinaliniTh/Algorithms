def remove_duplicate(string:str, res = '')->str:
    if len(string) == 0:
        return res
    if string[0] not in res:
        res += string[0]
    return remove_duplicate(string[1:], res)
res = remove_duplicate('aabbccdiio')
print(res)