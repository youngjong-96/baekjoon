# fizzbuzz

txt = [input() for _ in range(3)]

for i in range(3):
    if txt[i].isdigit():
        std = i
        break

if std == 0:
    num = int(txt[std]) + 3
elif std == 1:
    num = int(txt[std]) + 2
elif std == 2:
    num = int(txt[std]) + 1

if num % 3 == 0 and num % 5 == 0:
    print('FizzBuzz')
elif num % 3 == 0 and num % 5 != 0:
    print('Fizz')
elif num % 3 != 0 and num % 5 == 0:
    print('Buzz')
else:
    print(num)