def solution(num, n):
    r = num % n
    answer = 0
    if r == 0:
        answer = 1
    return answer