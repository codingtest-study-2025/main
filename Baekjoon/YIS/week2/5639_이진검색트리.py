import sys
sys.setrecursionlimit(10**6)  # 백준 입출력 관련 recursion 제한 해제

input = sys.stdin.readline
# sys.stdin = open('input.txt', 'r')

preorder_tree = []

while True:
    try:
        x = int(input())
        preorder_tree.append(x)
    except:
        break


def get_postoreder(start, end):

    # 인덱스가 넘어가면 종료
    if start >= end:
        return

    # 전위순회의 첫 번째 원소는 루트
    root = preorder_tree[start]

    # 왼쪽 서브트리에서 오른쪽 서브트리로 넘어가는 인덱스 찾기
    # 루트보다 큰 값이 처음 나오는 인덱스 찾기
    index = start + 1
    while index < end and preorder_tree[index] < root:
        index += 1

    # 재귀적으로 왼쪽 서브트리와 오른쪽 서브트리 처리 (왼쪽 > 오른쪽 > 루트)
    get_postoreder(start + 1, index)  # 왼쪽
    get_postoreder(index, end)  # 오른쪽
    print(root)  # 루트


start = 0
end = len(preorder_tree)
get_postoreder(start, end)
