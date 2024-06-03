import math


def test_function(x):
    def inner_function(x):
        print("Я в области видимости функции test_function")
    inner_function(x)


test_function(1)

# inner_function(1) - выдает ошибку, потому что функция является локальной.
