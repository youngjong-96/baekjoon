def solution(strArr):
    answer = []
    
    for Str in strArr:
        if "ad" not in Str:
            answer.append(Str)
        
    return answer