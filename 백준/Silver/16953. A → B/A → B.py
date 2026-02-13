import sys

#sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

A, B = map(int, input().split())

def recur(num, cnt):
    global result
    # 종료조건
    if num == B:
        result = max(result, cnt)
        return
    
    if num > B:
        return
    
    recur(num * 2, cnt + 1)
    recur(int(str(num) + '1'), cnt + 1)


result = -1
recur(A, 1)

print(result)