import sys

input = sys.stdin.readline

n = int(input().strip())
first = list(map(int, input().split()))
dp_max = first[:]
dp_min = first[:]

for i in range(n - 1):
    a, b, c = map(int, input().split())
    M1 = a + max(dp_max[0], dp_max[1])
    M2 = b + max(dp_max[0], dp_max[1], dp_max[2])
    M3 = c + max(dp_max[1], dp_max[2])
    dp_max[0], dp_max[1], dp_max[2] = M1, M2, M3

    m1 = a + min(dp_min[0], dp_min[1])
    m2 = b + min(dp_min[0], dp_min[1], dp_min[2])
    m3 = c + min(dp_min[1], dp_min[2])
    dp_min[0], dp_min[1], dp_min[2] = m1, m2, m3

print(max(dp_max), min(dp_min))