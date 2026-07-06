def solution(hp):
    j = hp // 5
    hp %= 5
    b = hp // 3
    hp %= 3
    answer = j + b + hp
    return answer