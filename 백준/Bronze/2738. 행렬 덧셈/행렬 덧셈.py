n, m = map(int, input().split())

arr1 = [list(map(int, input().split())) for _ in range(n)]
arr2 = [list(map(int, input().split())) for _ in range(n)]

arr = [[0] * m for _ in range(n)]

for i in range(n):
    for j in range(m):
        arr[i][j] = arr1[i][j] + arr2[i][j]

for i in range(n):
    for j in range(m):
        print(arr[i][j], end=" ")
    print()
        