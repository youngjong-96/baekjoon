def solution(num, k):
    n = []
    i = len(str(num))
    
    while num > 0:
        n.append((num % 10, i))
        num //= 10
        i -= 1
    
    for c, i in reversed(n):
        if c == k:
            return i
    else:
        return -1