# 괄호문자열

T = int(input())
for t in range(T):
    txt = input()

    result = 'YES'
    cnt = 0

    for i in txt:
        if i == '(':
            cnt += 1
        elif i == ')':
            cnt -= 1
        if cnt < 0:
            result = 'NO'
            break

    if cnt != 0:
        result = 'NO'

    print(result)