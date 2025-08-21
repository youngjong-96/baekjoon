# 웰컴 키트

# n = 참가자 수
n = int(input())

# 티셔츠 사이즈별 신청자 수
tlst = list(map(int, input().split()))

# t = 티셔츠 묶음 주문 수, p = 펜 묶음 주문 수
t, p = map(int, input().split())


# T = 티셔츠 최소 묶음 주문 수
T = 0
for i in tlst:
    if i % t == 0:
        T += (i // t)
    else:
        T += (i // t) + 1

# P = 펜 묶음 주문 수, r = 나머지 펜 주문 수
P = n // p
r = n % p

print(T)
print(P, r)