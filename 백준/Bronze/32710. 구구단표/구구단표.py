import sys

input = sys.stdin.readline

numbers = set()
for i in range(2, 10):
    for j in range(1, 10):
        numbers.add(i)
        numbers.add(j)
        numbers.add(i * j)

n = int(input().strip())
if n in numbers:
    print(1)
else:
    print(0)