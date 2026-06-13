def solution(myString, pat):
    l = len(myString)
    p = len(pat)
    idx = 0
    
    for i in range(l):
        if myString[i:i+p] == pat:
            idx = i+p
    
    answer = myString[:idx]
    
    return answer