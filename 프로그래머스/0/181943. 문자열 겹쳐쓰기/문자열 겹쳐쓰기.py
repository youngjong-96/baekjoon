def solution(my_string, overwrite_string, s):
    front = my_string[:s]
    tail = my_string[s + len(overwrite_string):]
    answer = front + overwrite_string + tail
    return answer