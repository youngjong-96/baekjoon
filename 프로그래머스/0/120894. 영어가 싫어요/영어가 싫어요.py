def solution(numbers):
    l = len(numbers)
    letters = {"zero" : '0', "one" : '1', "two" : '2', "three" : '3', "four" : '4',
               "five" : '5', "six" : '6', "seven" : '7', "eight" : '8', "nine" : '9'}
    answer = ''
    
    while numbers:
        for i in range(3, l):
            if numbers[0:i] in letters.keys():
                answer += letters[numbers[0:i]]
                numbers = numbers[i:]
                
    return int(answer)