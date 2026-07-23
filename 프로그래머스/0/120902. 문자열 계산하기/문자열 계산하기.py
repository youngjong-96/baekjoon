def solution(my_string):
    data = my_string.split()
    l = len(data)
    answer = int(data[0])
    
    for i in range(1, l, 2):
        if data[i] == "+":
            answer += int(data[i + 1])
        else:
            answer -= int(data[i + 1])
    
    return answer   