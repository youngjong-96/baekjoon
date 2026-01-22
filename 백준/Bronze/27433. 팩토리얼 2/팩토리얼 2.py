n = int(input())
result = 1
if n <= 1:
    result = 1
else:
    for i in range(2, n+1):
        result *= i
print(result)