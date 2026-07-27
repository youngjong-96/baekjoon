def solution(n):
    t = 1
    while n >= t * t:
        if n == t * t:
            return 1
        t += 1
    return 2