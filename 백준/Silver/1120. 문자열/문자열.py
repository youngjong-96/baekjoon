import sys
input = sys.stdin.readline

a, b = input().split()
la, lb = len(a), len(b)

def check(a, b):
    result = 0
    for i in range(la):
        if a[i] != b[i]:
            result += 1
    return result

if la == lb:
    print(check(a, b))
else:
    result = 50
    for i in range(lb-la+1):
        result = min(result, check(a, b[i:i+la]))
    print(result)
