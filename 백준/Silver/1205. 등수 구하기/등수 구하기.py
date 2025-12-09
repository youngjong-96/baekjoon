import sys
# https://www.acmicpc.net/problem/1205
#sys.stdin = open('sample_input.txt', 'r')
input = sys.stdin.readline

#####################

n, score, p = map(int, input().split())
ranks = list(map(int, input().split()))

if ranks and score <= ranks[-1] and len(ranks) == p:
    print(-1)
else:
    ranks.append(score)
    ranks.sort(reverse=True)
    ranks = ranks[:p + 1]

    result = [1]
    if len(ranks) < 2 and p >= 1:
        print(1)
    else:
        for i in range(1, len(ranks)):
            if ranks[i] == ranks[i-1]:
                result.append(result[i-1])
            else:
                result.append(i+1)
        print(result[ranks.index(score)])