import sys


input = sys.stdin.readline

txt = input().strip()
bomb = input().strip()
l = len(bomb)
lastC = bomb[-1]

stack = []

for i in txt:
    stack.append(i)
    if lastC >= i and "".join(stack[-l:]) == bomb:
        for _ in range(l):
            stack.pop()

if stack:
    print("".join(stack))
else:
    print('FRULA')