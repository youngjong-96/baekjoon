# n과 m

def recur(pick):
    if pick == m:
        print(*path)
        return

    for i in range(1, n+1):
        # path에 있는 마지막 숫자보다 i가 크거나 같다면,
        if not path:
            path.append(i)
            recur(pick+1)
            path.pop()
        else:
            if i >= path[-1]:
                path.append(i)
                recur(pick + 1)
                path.pop()

n, m = map(int, input().split())
path = []
recur(0)
