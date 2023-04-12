# fei bo na qi


def  feibo(number: int):
    a, b = 0, 1
    while b < number:
        print(a, end=' ')
        a, b = b, a + b

    print()

feibo(2000)
