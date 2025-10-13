def recur(cnt):
    if len(path) == m:
        print(*path)
        return

    for i in range(cnt, len(candidates)):
        path.append(candidates[i])
        recur(i)
        path.pop()


n, m = map(int, input().split())

numbers = list(map(int, input().split()))
candidates = sorted(list(set(numbers)))
path = []

recur(0)
