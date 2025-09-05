n = int(input())

# an = an-1 + 6(n-1) = 3n(n-1) + 1

result = 1
while result * 3 * (result - 1) + 1 < n:
    result += 1

print(result)