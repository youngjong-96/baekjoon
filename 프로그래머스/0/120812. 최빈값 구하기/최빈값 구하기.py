def solution(array):
    data = [0] * 1010
    
    for n in array:
        data[n] += 1
    
    result = []
    m = max(data)
    
    for i in range(1010):
        if data[i] == m:
            result.append(i)
    
    if len(result) > 1:
        answer = -1
    else:
        answer = result[0]
            
    return answer