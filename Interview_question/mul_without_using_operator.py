def find_mul(num1, num2):
    mul = 0
    for i in range(num1):
        mul += num2
    return mul
# print(find_mul(6,6))

def print_numbers_without_using_loop(num, n, res):
    if n >= num:
        return res + " " + str(n)
    res = res + " " + str(n)
    return print_numbers_without_using_loop(num, n+1, res)
# print(print_numbers_without_using_loop(100, 1, ""))

def pow(num, pow):
    res = 1
    for i in range(pow):
        res = res * num
    return res

num = lambda n,p : pow(n,p)
print(num(5,3))
