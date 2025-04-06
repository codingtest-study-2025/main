import sys
# sys.setrecursionlimit(10**6)  # 백준 입출력 관련 recursion 제한 해제

input = sys.stdin.readline
# sys.stdin = open('input.txt', 'r')

# 테스트케이스 개수
T = int(input())

# 케이스마다 그래프 생성
for _ in range(T):
    n = int(input())  # 노드 개수
    parent = [0] * (n + 1)  # 각 노드의 부모 저장
    for _ in range(n-1):
        a, b = map(int, input().split())
        parent[b] = a

    # 공통 조상을 구해야 하는 두 노드
    x, y = map(int, input().split())

    x_parents = [0, x]
    y_parents = [0, y]

    # 각 노드의 부모 리스트 생성
    while parent[x]:  # root에 도달할 때까지 반복
        x_parents.append(parent[x])
        x = parent[x]

    while parent[y]:
        y_parents.append(parent[y])
        y = parent[y]

    i = 1
    while True:
        if x_parents[-i] != y_parents[-i]:
            break
        i += 1

    print(x_parents[-i + 1])
