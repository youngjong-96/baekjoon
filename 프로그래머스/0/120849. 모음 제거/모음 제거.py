def solution(my_string):
    answer = ''
    for l in my_string:
        if l in ['a', 'e', 'i', 'o', 'u']:
            continue
        else:
            answer += l
    return answer