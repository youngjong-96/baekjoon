# 듣보잡

"""
김진영이 듣도 못한 사람의 명단과, 보도 못한 사람의 명단이 주어질 때, 듣도 보도 못한 사람의 명단을 구하는 프로그램을 작성하시오.
"""

# 첫째 줄에 듣도 못한 사람의 수 N, 보도 못한 사람의 수 M이 주어진다.
n, m = map(int, input().split())

nh = set()
ns = set()
# 이어서 둘째 줄부터 N개의 줄에 걸쳐 듣도 못한 사람의 이름과, N+2째 줄부터 보도 못한 사람의 이름이 순서대로 주어진다.
for _ in range(n):
    nh.add(input())

for _ in range(m):
    ns.add(input())

result = list(nh & ns)
result.sort()
print(len(result))
for name in result:
    print(name)