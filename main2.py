def test(*params):
    print(*params)


test(1, bool, [1, 2, 3])


def factorial(n):
    if n == 1:
        return n
    else:
        return n * factorial(n - 1)


print(factorial(int(input('Введите число: '))))
