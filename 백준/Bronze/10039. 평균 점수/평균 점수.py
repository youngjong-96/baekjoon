import sys

input = sys.stdin.readline

s = 0

for i in range(5):
    n = int(input().strip())
    if n < 40:
        n = 40
    s += n
print(s//5)