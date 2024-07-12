from self import self


def add_everything_up(a, b):
    self.a = a
    self.b = b
    a = (float, int, str)
    b = (float, int, str)

    try:
        total = add_everything_up()
        print(total)

    except TypeError:
        print(self.a, self.b)

print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))
