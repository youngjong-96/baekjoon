import sys

input = sys.stdin.readline

N, K = map(int, input().split())
Gs = list(map(int, input().split()))

def grade(score):
    if (score * 100) // N <= 4:
        return 1
    elif (score * 100) // N <= 11:
        return 2
    elif (score * 100) // N <= 23:
        return 3
    elif (score * 100) // N <= 40:
        return 4
    elif (score * 100) // N <= 60:
        return 5
    elif (score * 100) // N <= 77:
        return 6
    elif (score * 100) // N <= 89:
        return 7
    elif (score * 100) // N <= 96:
        return 8
    else:
        return 9

for i in Gs:
    print(grade(i), end=" ")