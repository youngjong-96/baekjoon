def solution(num_list, n):
    answer = []
    f = num_list[:n]
    b = num_list[n:]
    answer.extend(b)
    answer.extend(f)
    return answer