T = int(input())
for t in range(T):
    txt = input()

    score = 0
    cnt = 0

    for i in range(len(txt)):
        if txt[i] == 'O':
            cnt += 1
            score += cnt
        else:
            cnt = 0

    print(score)