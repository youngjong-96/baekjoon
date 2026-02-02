import sys

input = sys.stdin.readline

N, K = map(int, input().split())
data = list(map(int, input().split()))

result = sum(data[0:K])
hap = sum(data[0:K])

for i in range(N-K):
    hap = hap - data[i] + data[i+K]
    result = max(result, hap)

print(result)