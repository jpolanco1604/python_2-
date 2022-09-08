from audioop import mul
from functools import reduce


def run():
    my_list = [1, 2, 3, 4]
    multiplicador = reduce(lambda a, b: a*b, my_list)
    # multiplicador = 1
    # for i in my_list:
    #     multiplicador = i * multiplicador
    print(multiplicador)
    # squares = list(map(lambda x: x**2, my_list))
    # for i in my_list:
    #     squares.append(i**2)
    # odd = list(filter(lambda x: x%2 != 0, my_list))
    # odd = [i for i in my_list if i%2 != 0]
    # print(odd)
    # print(squares)


if __name__ == '__main__':
    run()