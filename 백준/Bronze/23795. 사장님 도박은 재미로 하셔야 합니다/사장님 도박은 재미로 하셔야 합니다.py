import sys

result = 0

while True:
    n = int(sys.stdin.readline().strip())
    if n == -1:
        break
    result += n

print(result)