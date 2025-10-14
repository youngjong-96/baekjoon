numbers = []
for i in range(666, 3000000):
    if '666' in str(i):
        numbers.append(int(i))

n = int(input())

print(numbers[n-1])