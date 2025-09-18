def Euclidean(a, b):
    while b != 0:
        a, b = b, a%b
    return a

a, b = map(int, input().split())

print(Euclidean(a, b))
print(abs(a * b) // Euclidean(a, b))
