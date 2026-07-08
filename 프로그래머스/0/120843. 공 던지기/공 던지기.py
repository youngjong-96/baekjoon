def solution(numbers, k):
    idx = 0
    l = len(numbers)
    
    while k > 1:
        k -= 1
        idx += 2
        if idx >= l:
            idx %= l
        
    return numbers[idx]