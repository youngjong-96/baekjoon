s = list(input())
n = len(s)
os = "".join(map(str, s))

rs=''
for i in range(n-1, -1, -1):
    rs += s[i]

if rs == os:
    print(1)
else:
    print(0)