vowels = 'aeiouAEIOU'
def count_vowels(string:str, count:int)->str:
    if len(string) == 0:
        return count
    if string[0] in vowels:
        count += 1
    return count_vowels(string[1:], count)

res= count_vowels('GOOGLE', count = 0)
print(res)

