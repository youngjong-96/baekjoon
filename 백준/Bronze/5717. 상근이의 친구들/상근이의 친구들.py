while True:
    num = list(map(int, input().split()))
    if num == [0, 0]:
        break
    else:
        print(sum(num))