from itertools import combinations

def solution(numbers):
    answer = 0
    lst = list(combinations(numbers, 2))
    for case in lst:
        x, y = case
        answer = max(answer, x * y)
            
    return answer