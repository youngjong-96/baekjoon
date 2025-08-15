# 그룹 단어란 단어에 존재하는 모든 문자에 대해서, 각 문자가 연속해서 나타나는 경우만을 말한다. 
# 예를 들면, ccazzzzbb는 c, a, z, b가 모두 연속해서 나타나고, kin도 k, i, n이 연속해서 나타나기 때문에 그룹 단어이지만, 
# aabbbccb는 b가 떨어져서 나타나기 때문에 그룹 단어가 아니다.

# 단어 N개를 입력으로 받아 그룹 단어의 개수를 출력하는 프로그램을 작성하시오.

# 첫째 줄에 단어의 개수 N이 들어온다. N은 100보다 작거나 같은 자연수이다. 둘째 줄부터 N개의 줄에 단어가 들어온다.

n = int(input())

cnt = 0


for _ in range(n):
    word = input()
    
    # 이전에 나온 단어 확인 용
    stack = [word[0]]
    
    for i in range(1, len(word)):
        # 전 단어와 같다면 패스
        if word[i] == word[i-1]:
            pass
        # 다르다면
        else:
            # 전에 나온 적이 있다면 그룹 단어가 아니다
            if word[i] in stack:
                break
            else:
                stack.append(word[i])
    else:
        cnt += 1

print(cnt)