import sys

input = sys.stdin.readline

text = input()
result = ""

for t in text:
    if t.upper() == t:
        t = t.lower()
    else:
        t = t.upper()
    result += t
print(result)