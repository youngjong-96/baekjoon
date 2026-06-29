def solution(slice, n):
    answer = 0
    
    for i in range(100):
        if slice * i >= n:
            answer = i
            break
            
    return answer