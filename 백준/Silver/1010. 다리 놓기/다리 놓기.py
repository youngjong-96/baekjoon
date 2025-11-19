import sys

T = int(sys.stdin.readline().strip())
for t in range(T):
    n, m = map(int, sys.stdin.readline().strip().split())

    top = 1  
    bottom = 1  

    k = min(n, m - n)

    for i in range(k):
        top *= (m - i)
        bottom *= (i + 1)

    result = top // bottom
    print(result)