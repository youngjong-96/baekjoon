def solution(quiz):
    answer = []
    for q in quiz:
        data = q.split()
        if data[1] == "+":
            if int(data[0]) + int(data[2]) == int(data[4]):
                answer.append('O')
            else:
                answer.append('X')
        else:
            if int(data[0]) - int(data[2]) == int(data[4]):
                answer.append('O')
            else:
                answer.append('X')
    return answer