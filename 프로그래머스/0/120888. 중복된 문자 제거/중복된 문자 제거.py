def solution(my_string):
    answer = ''
    for s in my_string:
        if s in answer:
            continue
        else:
            answer += s
    return answer