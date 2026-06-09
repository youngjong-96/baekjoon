def solution(str_list):
    answer = []
    l = len(str_list)
    
    for i in range(l):
        if str_list[i] == 'l':
            answer = str_list[:i]
            break
        elif str_list[i] == 'r':
            answer = str_list[i+1:]
            break
    return answer