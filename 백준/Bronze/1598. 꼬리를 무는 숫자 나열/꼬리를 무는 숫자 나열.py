import sys
input = sys.stdin.readline

a, b = map(int, input().split())
v, h = 0, 0
if a > b:
    a, b = b, a

va = a // 4
vb = b // 4

ha = a % 4
hb = b % 4

if ha == 0:
    ha = 4
    va -= 1
if hb == 0:
    hb = 4
    vb -= 1

v = vb - va
if hb > ha:
    h = hb - ha
else:
    h = ha - hb

print(v + h)