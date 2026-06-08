def solution(my_string, indices):
    answer = ''
    l = len(my_string)
    idx = list(set(range(l)) - set(indices))
    
    for i in sorted(idx):
        answer += my_string[i]
        
    return answer