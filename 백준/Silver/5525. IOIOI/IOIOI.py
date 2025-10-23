import sys

n = int(sys.stdin.readline().strip())
m = int(sys.stdin.readline().strip())
S = sys.stdin.readline().strip()

s = 'I' + 'OI' * n
l = len(s)
cnt = 0

for i in range(0, m+1-l):
    if s == S[i:i+l]:
        cnt += 1

print(cnt)