import sys

input = sys.stdin.readline

card_a = list(map(int, input().split()))
card_b = list(map(int, input().split()))
n = len(card_a)
score_a = 0
score_b = 0
last_winner = 'D'

for i in range(n):
    if card_a[i] > card_b[i]:
        score_a += 3
        last_winner = 'A'
    elif card_a[i] < card_b[i]:
        score_b += 3
        last_winner = 'B'
    else:
        score_a += 1
        score_b += 1

print(score_a, score_b)
if score_a > score_b:
    print('A')
elif score_a < score_b:
    print('B')
elif score_a == score_b and last_winner == 'D':
    print('D')
else:
    print(last_winner)