def solution(l, r):
    answer = []
    
    for i in range(l, r + 1):
        stri = str(i)
        seti = set(stri)
        setl = len(seti)
        if (setl == 1 and '0' in seti) or (setl == 1 and '5' in seti) or (setl == 2 and '0' in seti and '5' in seti):
            answer.append(i)
    
    if not answer:
        answer = [-1]
        
    return answer