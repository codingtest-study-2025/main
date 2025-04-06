import sys
input = sys.stdin.readline  # 일반 input보다 훨씬 빠름

sys.setrecursionlimit(10**6)  # 백준 입출력 관련 recursion 제한 해제

# sys.stdin = open('input.txt', 'r')

# 이진 트리를 딕셔너리로 표현
n = int(input().strip())
tree = {}

for i in range(n):
    root, left, right = input().split()
    tree[root] = [left, right]


def 전위순회(root):
    if root == '.':
        return

    print(root, end="")  # 루트
    전위순회(tree[root][0])  # 왼쪽 자식
    전위순회(tree[root][1])  # 오른쪽 자식


def 중위순회(root):
    if root == '.':
        return

    중위순회(tree[root][0])  # 왼쪽 자식
    print(root, end="")  # 루트
    중위순회(tree[root][1])  # 오른쪽 자식


def 후위순회(root):
    if root == '.':
        return

    후위순회(tree[root][0])  # 왼쪽 자식
    후위순회(tree[root][1])  # 오른쪽 자식
    print(root, end="")  # 루트


전위순회('A')
print()
중위순회('A')
print()
후위순회('A')
