ISBN = input()

c = 0
idx = 0

for i in range(13):
    if ISBN[i] == '*':
        idx = int(i)
    else:
        if int(i) % 2 == 0:
            c += int(ISBN[i])
        else:
            c += int(ISBN[i]) * 3

m = int(ISBN[-1])

if idx % 2 == 0:
    result = -c % 10
else:
    result = (-7 * c) % 10

print(result)
