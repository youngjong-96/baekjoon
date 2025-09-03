# Hashing

"""
1. a~z에 각각 1~26의 번호를 부여하고 31을 곱해서 더한다.
2. 그 수를 1234567891로 나눈 나머지를 출력한다.
"""

import sys

L = int(sys.stdin.readline().strip())

letter = sys.stdin.readline().strip()

key = {}

# 'a' = 97
for i in range(1, 27):
    key[chr(96 + i)] = i

result = 0

for i in range(L):
    result += key[letter[i]] * (31 ** i)

print(result % 1234567891)