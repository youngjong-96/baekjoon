def solution(my_str, n):
    answer = []
    l = len(my_str)
    for i in range(0, l, n):
        answer.append(my_str[i:i+n])
    return answer