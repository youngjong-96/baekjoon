# 단어 정렬
"""
알파벳 소문자로 이루어진 N개의 단어가 들어오면 아래와 같은 조건에 따라 정렬하는 프로그램을 작성하시오.

길이가 짧은 것부터
길이가 같으면 사전 순으로
단, 중복된 단어는 하나만 남기고 제거해야 한다.
"""
import sys


# 단어들 저장할 배열 생성
# 중복 없이 입력받기 위해 set로 생성
words = [set() for _ in range(51)]

n = int(sys.stdin.readline().strip())

# 단어의 길이를 idx로 같은 길이의 단어들을 words 리스트에 추가한다
for i in range(n):
    word = sys.stdin.readline().strip()
    words[len(word)].add(word)

# words 리스트를 순회하며
for i in range(len(words)):
    # 빈 리스트는 제외
    if words[i]:
        # 리스트로 변환 후 정렬하고 출력한다
        words[i] = list(words[i])
        words[i].sort()
        for j in range(len(words[i])):
            print(words[i][j])