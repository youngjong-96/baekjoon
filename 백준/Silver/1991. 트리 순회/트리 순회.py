# 트리 순회

"""
이진 트리를 입력받아 전위 순회(preorder traversal), 중위 순회(inorder traversal), 후위 순회(postorder traversal)한
결과를 출력하는 프로그램을 작성하시오.
"""
import sys


def pre_order(start):
    if start == '.':
        return
    else:
        print(start, end="")
        pre_order(tree[start][0])
        pre_order(tree[start][1])

def mid_order(start):
    if start == '.':
        return
    else:
        mid_order(tree[start][0])
        print(start, end="")
        mid_order(tree[start][1])

def post_order(start):
    if start == '.':
        return
    else:
        post_order(tree[start][0])
        post_order(tree[start][1])
        print(start, end="")

# 노드 = n
n = int(sys.stdin.readline().strip())

# {'A': ['B', 'C'], 'B': ['D', '.'], 'C': ['E', 'F'], 'E': ['.', '.'], 'F': ['.', 'G'], 'D': ['.', '.'], 'G': ['.', '.']}
tree = {}

for i in range(n):
    p, l, r = sys.stdin.readline().strip().split()

    tree.setdefault(p, [l, r])

pre_order('A')
print()
mid_order('A')
print()
post_order('A')