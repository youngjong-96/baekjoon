while True:
    numbers = list(map(int, input().split()))
    numbers.sort()
    a, b, c = numbers[0], numbers[1], numbers[2]

    if a == 0 and b == 0 and c == 0:
        break

    if c**2 == a**2 + b**2:
        print('right')
    else:
        print('wrong')
