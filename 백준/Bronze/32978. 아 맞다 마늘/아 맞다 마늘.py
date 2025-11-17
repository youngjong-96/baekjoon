import sys

n = int(sys.stdin.readline().strip())
ingredients = sys.stdin.readline().strip().split()
food = sys.stdin.readline().strip().split()

for f in food:
    ingredients.remove(f)

print(*ingredients)