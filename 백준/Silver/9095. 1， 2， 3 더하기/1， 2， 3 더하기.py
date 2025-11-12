def recur(n):
    global result

    if n == 0:
        result += 1
        return

    if n < 0:
        return
    
    recur(n-1)
    recur(n-2)
    recur(n-3)

T = int(input())
for t in range(T):
    n = int(input())
    result = 0
    recur(n)
    print(result)