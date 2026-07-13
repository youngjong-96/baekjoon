def f(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
        
    return result

def solution(n):
    answer = 0
    for i in range(n + 1):
        if f(i) <= n:
            answer = i
        else:
            break
    
    return answer