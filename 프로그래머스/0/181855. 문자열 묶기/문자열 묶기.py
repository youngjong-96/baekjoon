def solution(strArr):
    answer = 0
    cnt = [0] * 31
    
    for s in strArr:
        cnt[len(s)] += 1
    
    for i in range(31):
        answer = max(answer, cnt[i])
        
    return answer