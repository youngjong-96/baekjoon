n = int(input())

result = -1

for five_count in range(n // 5, -1, -1):
    
    remainder = n - (five_count * 5)

    if remainder % 3 == 0:
        three_count = remainder // 3
        result = five_count + three_count
        break

print(result)