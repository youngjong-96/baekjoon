def solution(myString, pat):
    answer = 0
    f = ''
    for p in pat:
        if p == 'A':
            f += 'B'
        else:
            f += 'A'
    
    l = len(myString)
    lf = len(f)
    
    for i in range(l):
        if myString[i:i+lf] == f:
            answer = 1
            break
            
    return answer