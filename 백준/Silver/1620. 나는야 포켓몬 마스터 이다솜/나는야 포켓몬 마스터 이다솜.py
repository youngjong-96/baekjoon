import sys

# 첫째 줄에는 도감에 수록되어 있는 포켓몬의 개수 N이랑 내가 맞춰야 하는 문제의 개수 M이 주어져.
n, m = map(int, sys.stdin.readline().strip().split())

poketmon_by_number = {}
poketmon_by_name = {}

# N개의 줄에 포켓몬의 번호가 1번인 포켓몬부터 N번에 해당하는 포켓몬까지 한 줄에 하나씩 입력으로 들어와.
for i in range(1, n + 1):
    name = sys.stdin.readline().strip()
    poketmon_by_number[str(i)] = name  
    poketmon_by_name[name] = str(i) 

# 그 다음 줄부터 총 M개의 줄에 내가 맞춰야하는 문제가 입력으로 들어와.
for _ in range(m):
    q = sys.stdin.readline().strip()
    if q.isdigit():
        print(poketmon_by_number[q])
    else:
        print(poketmon_by_name[q])