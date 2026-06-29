def solution(numbers):
    l = len(numbers)
    s = 0
    
    for n in numbers:
        s += n
    
    answer = s / l
    
    return answer