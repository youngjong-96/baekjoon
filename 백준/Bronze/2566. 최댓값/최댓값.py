arr = [list(map(int, input().split())) for _ in range(9)]

max_v = arr[0][0]
max_i = 1
max_j = 1

for i in range(9):
    for j in range(9):
        if arr[i][j] > max_v:
            max_v = arr[i][j]
            max_i = i + 1
            max_j = j + 1

print(max_v)
print(f'{max_i} {max_j}')
