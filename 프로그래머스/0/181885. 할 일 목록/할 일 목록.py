def solution(todo_list, finished):
    answer = []
    l = len(todo_list)
    
    for i in range(l):
        if not finished[i]:
            answer.append(todo_list[i])
            
    return answer