s = input().upper()
s_set = set(s)

max_v = 0
r_dict = {}
# {'B': 1, 'A': 3}
result = ""

for i in s_set:
    r_dict.setdefault(i, s.count(i))

for key, value in r_dict.items():
    if max_v < value:
        max_v = value
        result = key

if list(r_dict.values()).count(max_v) >= 2:
    result = "?"

print(result)