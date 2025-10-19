import sys
from collections import Counter

n = int(sys.stdin.readline().strip())
numbers = []
hap = 0

for _ in range(n):
    num = int(sys.stdin.readline().strip())
    hap += num
    numbers.append(num)
numbers.sort()

print(round(hap/n))
print(numbers[n//2])

counts = Counter(numbers)
modes = counts.most_common()
if len(modes) > 1 and modes[0][1] == modes[1][1]:
    # 최빈값이 여러 개인 경우
    max_freq = modes[0][1]
    all_modes = [num for num, freq in modes if freq == max_freq]
    all_modes.sort()
    print(all_modes[1]) # 두 번째로 작은 값
else:
    # 최빈값이 하나인 경우
    print(modes[0][0])
    
print(numbers[-1] - numbers[0])