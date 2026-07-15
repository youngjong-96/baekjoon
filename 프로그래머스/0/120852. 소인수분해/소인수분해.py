def issosu(n):
    if n == 2:
        return 1
    
    for i in range(2, n):
        if n % i == 0:
            return 0
        
    return 1

def solution(n):
    answer = []
    while n > 1:
        for i in range(n, 1, -1):
            if n % i == 0 and issosu(i):
                answer.append(i)
                n //= i
                break
                    
    return sorted(list(set(answer)))