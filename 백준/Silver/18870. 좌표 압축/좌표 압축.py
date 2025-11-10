import sys

n = int(sys.stdin.readline().strip())
xi = list(map(int, sys.stdin.readline().strip().split()))

unique_xi = sorted(list(set(xi)))

hashmap = {}

for idx, value in enumerate(unique_xi):
    hashmap[value] = idx

for i in xi:
    print(hashmap[i], end=" ")