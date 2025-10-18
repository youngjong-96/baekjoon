import sys

def solve():
    n = int(sys.stdin.readline().strip())
    
    stack = []
    result = []
    current_num = 1 # 1부터 n까지 push할 숫자
    
    for _ in range(n):
        target = int(sys.stdin.readline().strip())
        
        # target을 만날 때까지 push
        while current_num <= target:
            stack.append(current_num)
            result.append('+')
            current_num += 1
            
        # 스택의 top이 target과 일치하는지 확인
        if stack and stack[-1] == target:
            stack.pop()
            result.append('-')
        else:
            # 스택의 top이 target이 아니면 (target보다 크면) 불가능
            print('NO')
            return

    # 모든 과정을 마쳤으면 결과 출력
    for op in result:
        print(op)

solve()