h, m, s = map(int, input().split())
time = int(input())

t_m = time // 60
t_s = time % 60

t_h = t_m // 60
t_m = t_m % 60

h += t_h
m += t_m
s += t_s

m += s // 60
s %= 60

h += m // 60
m %= 60

h %= 24

print(h, m, s)