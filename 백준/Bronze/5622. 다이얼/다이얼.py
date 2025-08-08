s = list(input())


dial = {3: ['A', 'B', 'C'],
        4: ['D', 'E', 'F'],
        5: ['G', 'H', 'I'],
        6: ['J', 'K', 'L'],
        7: ['M', 'N', 'O'],
        8: ['P', 'Q', 'R', 'S'],
        9: ['T', 'U', 'V'],
        10: ['W', 'X', 'Y', 'Z']
}

result = 0

for word in s:
    for time, letter in dial.items():
        if word in letter:
            result += time
            break

print(result)