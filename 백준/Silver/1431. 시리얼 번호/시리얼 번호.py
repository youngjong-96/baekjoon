import sys

input = sys.stdin.readline

n = int(input().strip())
snums = []

for _ in range(n):
    snum = input().strip()
    hap = 0
    for i in snum:
        if i.isnumeric():
            hap += int(i)
    snums.append((len(snum), hap, snum))

sorted_snums = sorted(snums, key=lambda x: (x[0], x[1], x[2]))

# print(sorted_snums)
for result in sorted_snums:
    print(result[2])