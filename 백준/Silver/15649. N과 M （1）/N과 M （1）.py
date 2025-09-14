# n과 m(1)

n, m = map(int, input().split())
path = []
used = [0] * (n + 1)

def permutation(e):
    if e == m:
        print(*path)
        return

    for candidate in range(1, n+1):
        if used[candidate]:
            continue

        used[candidate] = 1
        path.append(candidate)
        permutation(e + 1)
        path.pop()
        used[candidate] = 0

permutation(0)