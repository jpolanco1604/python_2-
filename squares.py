def run():
    # squares = []
    # for i in range (1, 101):
    #     if i%3 != 0:
    #             squares.append(i**2)
    # print(squares)

    squares = [i for i in range(1, 100) if i%6 == 0 & i%9 == 0 & i%4 == 0]

    print(squares)


if __name__ == '__main__':
    run()