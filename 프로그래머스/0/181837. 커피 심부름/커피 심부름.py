def solution(order):
    answer = 0
    for o in order:
        if o in ["iceamericano", "americanoice", "hotamericano", "americanohot", "americano", "anything"]:
            answer += 4500
        else:
            answer += 5000
        
    return answer