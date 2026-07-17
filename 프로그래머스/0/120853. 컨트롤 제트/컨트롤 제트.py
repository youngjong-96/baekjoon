def solution(s):
    answer = 0
    lst = s.split()
    idx = len(lst) - 1
    
    while idx >= 0:
        if idx == -1:
            break
        if lst[idx] == 'Z':
            idx -= 2
        else:
            answer += int(lst[idx])
            idx -= 1
            
    return answer