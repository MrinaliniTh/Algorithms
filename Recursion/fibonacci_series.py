                #                fib(5)
                #           2    /  +   \ 1 = 3
                #         fib(4)         fib(3)
                #         /  \             \
                #    fib(3)   fib(2)        1
                #     /         \
                #    1     +    1 = 2
def fib(num: int) -> int:
    if num == 0:
        return 0
    if num == 2 or num == 3:
        return 1
    return fib(num-1) + fib(num-2)

res = fib(5)
print(res)
    