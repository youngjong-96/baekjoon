def solution(strArr):
    answer = []
    l = len(strArr)
    
    for i in range(l):
        if i % 2 == 0:
            answer.append(strArr[i].lower())
        else:
            answer.append(strArr[i].upper())
    return answer