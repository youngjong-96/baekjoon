def solution(cipher, code):
    answer = ''
    l = len(cipher)
    for i in range(code - 1, l, code):
        answer += cipher[i]
    return answer