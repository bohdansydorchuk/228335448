

import datetime


"""1 exercice"""
start = int(input('enter the start of calculation: '))
finish = int(input('enter the start of calculation: '))

def counter(start: int, finish: int) -> int:
    list = [start, finish]
    list = sorted(list)
    result = sum(range(list[0], list[1] + 1))
    return result

print(counter(start, finish))

"""2 exercice"""

def time_convert(sec: int):
    result = datetime.timedelta(seconds=sec)
    return result
print( time_convert (360000) )


"""3 exercise"""
list = [1, 3, 4, 6, 7, 8, 12, 2]

def for_counter(list: list) -> int or float:
    sum = 0
    for i in list:
        sum += i
    return sum

print(for_counter(list))

list = [1, 3, 4, 6, 7, 8, 12, 2]

def while_counter(list: list) -> int or float:
    sum = 0
    while len(list) != 0:
        sum += list()
    return sum

print(while_counter(list))

list = [1, 3, 4, 6, 7, 8, 12, 2]

def recurs_counter(list: list) -> int or float:
    if list == []:
        return 0
    else:
        sum = recurs_counter(list[1:])
        sum = sum + list[0]
        return sum

print(recurs_counter(list))

def time_convert(sec: int):
    result = datetime.timedelta(seconds=sec)
    return result
print( time_convert (360000) )

"""4 exersice"""


def recurs_fibo(n: int) -> int:
    if n in (1, 2):
        return 1
    return recurs_fibo(n - 1) + recurs_fibo(n - 2)


print(f'{recurs_fibo(5) = }')


"""5 exersice"""

"""first decor"""

print('first decor:')


def ingr_burger(decor_this) -> any:
    def ingr_tomato():
        print('tomato')

    def ingr_meat():
        print('meat')

    def ingr_chees():
        print('chees')

    def ingr_bread():
        print('bread')
    return ingr_tomato(), ingr_meat(), ingr_chees(), ingr_bread()


@ingr_burger
def burger() -> None:
    return

"""second decor"""

print('second decor:')


def ingr_tomato(decor_this):
    print('tomato')


def ingr_meat(decor_this):
    print('meat')


def ingr_chees(decor_this):
    print('chees')


def ingr_bread(decor_this):
    print('bread')


@ingr_bread
@ingr_chees
@ingr_meat
@ingr_tomato
def burger() -> None:
    return