import sys

n, m = map(int, sys.stdin.readline().split())
pack_price_lst = []
one_price_lst = []

for i in range(m):
    six, one = map(int, sys.stdin.readline().split())
    pack_price_lst.append(six)
    one_price_lst.append(one)
six = min(pack_price_lst)
one = min(one_price_lst)

result = 0

if one * 6 < six:
    result = one * n
else:
    result += six * (n // 6)
    if one * (n % 6) < six:
        result += one * (n % 6)
    else:
        result += six
print(result)