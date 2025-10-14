import sys

while True:
    txt = sys.stdin.readline().rstrip() 
    if txt == '.':
        break

    stack = []
    is_balanced = True  

    for char in txt:
        if char == '(' or char == '[':
            stack.append(char)
        elif char == ')':
            # 스택이 비어있거나, 짝이 맞지 않으면 불균형
            if not stack or stack.pop() != '(':
                is_balanced = False
                break
        elif char == ']':
            # 스택이 비어있거나, 짝이 맞지 않으면 불균형
            if not stack or stack.pop() != '[':
                is_balanced = False
                break

    # 루프가 끝난 후, 스택이 비어있지 않으면 여는 괄호가 남은 것이므로 불균형
    if is_balanced and not stack:
        print('yes')
    else:
        print('no')