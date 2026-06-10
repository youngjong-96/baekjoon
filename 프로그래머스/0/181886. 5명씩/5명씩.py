def solution(names):
    answer = []
    l = len(names)
    
    for i in range(0, l, 5):
        answer.append(names[i])
        
    return answer