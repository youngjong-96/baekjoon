import sys

def recursion(s, l, r):
    global cnt
    cnt += 1
    if l >= r: return 1
    elif s[l] != s[r]: return 0
    else: return recursion(s, l+1, r-1)

def isPalindrome(s):
    return recursion(s, 0, len(s)-1)

T = int(sys.stdin.readline().strip())
for t in range(1, T+1):
    s = sys.stdin.readline().strip()
    cnt = 0
    print(isPalindrome(s), cnt)