def solution(array):
    answer = 0
    for n in array:
        for t in str(n):
            if t == '7':
                answer += 1
    return answer