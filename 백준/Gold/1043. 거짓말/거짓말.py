import sys

input = sys.stdin.readline

N, M = map(int, input().split())
know_true = list(map(int, input().split()))
know_true_list = know_true[1:] if know_true[0] > 0 else []

parent = list(range(N + 1))

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    root_a = find(a)
    root_b = find(b)
    if root_a != root_b:
        if root_a < root_b:
            parent[root_b] = root_a
        else:
            parent[root_a] = root_b

# 1. 파티 정보를 미리 저장하고 사람들을 union
parties = []
for _ in range(M):
    p_info = list(map(int, input().split()))
    p_people = p_info[1:]
    parties.append(p_people)
    
    for i in range(len(p_people) - 1):
        union(p_people[i], p_people[i+1])

# 2. 진실을 아는 사람들의 루트 노드 파악
know_roots = set()
for person in know_true_list:
    know_roots.add(find(person))

# 3. 각 파티를 돌며 진실을 아는 그룹에 속해 있는지 확인
ans = 0
for party in parties:
    can_lie = True
    for p in party:
        if find(p) in know_roots:
            can_lie = False
            break
    if can_lie:
        ans += 1

print(ans)