def solution(myString, pat):
    answer = 0
    m = len(myString)
    p = len(pat)
    myString = myString.lower()
    pat = pat.lower()
    
    if p > m:
        pass
    else:
        for i in range(0, m):
            if myString[i:i+p] == pat:
                answer = 1
                break
                
    return answer