def is_prime(func):
    def wrapper(*args):
        result = func(*args)
        k = 0
        for i in range(1, result+1):
            if result % i == 0:
                k += 1
        if k == 2:
            print('Простое')
        else:
            print('Составное')
        return result
    return wrapper

@is_prime
def sum_three(a, b, c):
    return a + b + c

result = sum_three(2, 3, 6)
print(result)