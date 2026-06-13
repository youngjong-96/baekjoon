def solution(myString, pat):
    answer = 0
    l = len(myString)
    p = len(pat)
    
    for i in range(l):
        if myString[i:i+p] == pat:
            answer += 1
            
    return answer