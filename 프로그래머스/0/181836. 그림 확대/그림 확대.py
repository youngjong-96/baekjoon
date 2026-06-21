def solution(picture, k):
    answer = []
    
    for pic in picture:
        w = ''
        for p in pic:
            w += p * k
        for _ in range(k):
            answer.append(w)
        
    return answer