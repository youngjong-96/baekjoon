# 의석이는 어디가 아픈가봐


# 글자 입력 받기
arr = [list(map(str, input())) for _ in range(5)]
max_l = 0

for i in range(len(arr)):
    if max_l < len(arr[i]):
        max_l = len(arr[i])

result = ""
# 세로로 읽기
for i in range(max_l):
    for j in range(len(arr)):
        if i < len(arr[j]):  # 해당 행의 길이가 짧으면 패스하는 조건
            result += arr[j][i]

print(result)
