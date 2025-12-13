import sys

#sys.stdin = open('sample_input.txt', 'r')
input = sys.stdin.readline

n = int(input())
switches = list(map(int, input().split()))
ns = int(input())

def change_switch(idx):
    if switches[idx] == 1:
        switches[idx] = 0
    else:
        switches[idx] = 1

for _ in range(ns):
    sex, switch = map(int, input().split())
    idx = switch - 1
    m = 1
    if sex == 1:
        while switch * m <= n:
            change_switch(switch * m - 1)
            m += 1
    else:
        change_switch(idx)
        while idx + m < n and idx - m >= 0:
            if switches[idx - m] == switches[idx + m]:
                change_switch(idx - m)
                change_switch(idx + m)
                m += 1
            else:
                break
if n > 20:
    for i in range(0, n, 20):
        print(*switches[i:i+20])
else:
    print(*switches)