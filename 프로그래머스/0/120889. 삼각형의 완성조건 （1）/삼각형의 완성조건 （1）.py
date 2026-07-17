def solution(sides):
    l = max(sides)
    if sum(sides) - l > l:
        return 1
    return 2