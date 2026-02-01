import sys

input = sys.stdin.readline

times = [int(input().strip()) for i in range(4)]

print(sum(times)//60)
print(sum(times)%60)