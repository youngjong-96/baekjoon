def ishap(n):
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            return 1
    return 0

def solution(n):
    answer = 0
    for i in range(2, n + 1):
        if ishap(i):
            answer += 1
            
    return answer