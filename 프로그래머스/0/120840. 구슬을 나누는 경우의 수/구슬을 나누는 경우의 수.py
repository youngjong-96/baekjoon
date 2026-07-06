def factorial(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def solution(balls, share):
    if balls == share:
        return 1
    else:
        answer = factorial(balls) / (factorial(share) * factorial(balls - share))
        
    return answer