import sys

def find(target):
    left = 0
    right = len(numbers) - 1
    while left <= right:
        mid = (left + right) // 2

        if numbers[mid] == target:
            return 1

        if target > numbers[mid]:
            left = mid + 1
        else:
            right = mid - 1
    return 0

n = int(sys.stdin.readline().strip())
numbers = list(map(int, sys.stdin.readline().strip().split()))
numbers.sort()

m = int(sys.stdin.readline().strip())
targets = list(map(int, sys.stdin.readline().strip().split()))

for target in targets:
    print(find(target))