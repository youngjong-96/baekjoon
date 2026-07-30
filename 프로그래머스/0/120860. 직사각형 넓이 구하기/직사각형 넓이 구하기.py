def solution(dots):
    return abs(sorted(dots)[0][0] - sorted(dots)[2][0]) * abs(sorted(dots)[0][1] - sorted(dots)[1][1])