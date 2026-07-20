def solution(array, n):
    gap = []
    
    for i in array:
        gap.append(abs(i - n))
    
    answer_lst = []
    
    for idx in range(len(gap)):
        if gap[idx] == min(gap):
            answer_lst.append(idx)
    
    if len(answer_lst) > 1:
        answer = array[answer_lst[0]]
        for idx in answer_lst:
            if array[idx] < answer:
                answer = array[idx]
    else:
        answer = array[answer_lst[0]]
        
    return answer